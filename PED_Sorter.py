import re
import sys
import json
import os
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

import pandas as pd
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import QProcess, QFileInfo

from PED_design import Ui_MainWindow
from tags_window_design import Ui_TagsWindow


class TagsManager:
    def __init__(self):
        self.exec_dir = Path(__file__).parent.absolute()
        self.tags_file = self.exec_dir / 'file_types_base.json'
        self.tags_data = self._load_tags()

    def _load_tags(self):
        """Загружает теги из файла или создает новый с дефолтными значениями"""
        default_tags = {
            "1": {
                "type": "Локальная смета",
                "name_tags": [
                    "локальная смета",
                    "лс",
                    "лc"
                ],
                "internal_tags": [
                    "локальная смета"
                ],
                "mask": "ЛС-ГС-ПНо-ПНл-ВЕРНН-КОММ"
                },
        }
        try:
            if not self.tags_file.exists():
                os.makedirs(self.tags_file.parent, exist_ok=True)
                self._save_tags(default_tags)
                return default_tags
            
            with open(self.tags_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Ошибка загрузки тегов: {e}")
            return default_tags

    def _save_tags(self, data):
        """Сохраняет теги в файл"""
        with open(self.tags_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_type_data(self, type_id):
        """Возвращает данные по типу файла"""
        return self.tags_data.get(str(type_id))

    def add_tag(self, type_id, new_tag, tag_area):
        """Добавляет новый тег для типа"""
        type_id = str(type_id)
        if type_id not in self.tags_data:
            return False
        if new_tag not in self.tags_data[type_id][tag_area]:
            self.tags_data[type_id][tag_area].append(new_tag)
            self._save_tags(self.tags_data)
            return True
        return False

    def remove_tag(self, type_id, tag_to_remove, tag_area):
        """Удаляет тег у указанного типа"""
        type_id = str(type_id)
        if type_id in self.tags_data and tag_to_remove in self.tags_data[type_id][tag_area]:
            self.tags_data[type_id][tag_area].remove(tag_to_remove)
            self._save_tags(self.tags_data)
            return True
        return False

    def change_mask(self, type_id, new_mask):
        type_id = str(type_id)
        if type_id not in self.tags_data:
            return False
        self.tags_data[type_id]["mask"] = new_mask
        self._save_tags(self.tags_data)
        return True


class TagsWindow(QtWidgets.QMainWindow):
    def __init__(self, type_id, tags_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_TagsWindow()
        self.ui.setupUi(self)
        self.type_id = str(type_id)
        self.tags_manager = tags_manager
        self._setup_ui()
        self.logger = setup_logging()
        self._connect_signals()

    def _setup_ui(self):
        """Заполняет окно данными"""
        type_data = self.tags_manager.get_type_data(self.type_id)
        if type_data:
            self.ui.type_label.setText(type_data["type"])
            self.ui.TagList.addItems(type_data["name_tags"])
            self.ui.TagList_2.addItems(type_data["internal_tags"])
            self.ui.mask_lineEdit.setText(type_data["mask"])
        
    def _connect_signals(self):
        """Подключает сигналы кнопок"""
        self.ui.add_tag.clicked.connect(lambda: self._add_tag('name_tags'))
        self.ui.add_tag_2.clicked.connect(lambda: self._add_tag('internal_tags'))
        self.ui.delete_tag.clicked.connect(lambda: self._delete_tag('name_tags'))
        self.ui.delete_tag_2.clicked.connect(lambda: self._delete_tag('internal_tags'))
        self.ui.tag_lineEdit.returnPressed.connect(self._add_tag)
        self.ui.save_mask.clicked.connect(self._change_mask)
    
    def _change_mask(self):
        """"Корректирует маску"""
        new_mask = self.ui.mask_lineEdit.text().strip()
        if new_mask:
            self.tags_manager.change_mask(self.type_id, new_mask)

    def _add_tag(self, tag_area):
        """Добавляет новый тег"""
        self.logger.debug(f'ДОБАВЛЯЕМ НОВЫЙ ТЭГ: {tag_area}')
        if tag_area == 'name_tags':
            new_tag = self.ui.tag_lineEdit.text().strip()
            if new_tag:
                if self.tags_manager.add_tag(self.type_id, new_tag, tag_area):
                    self.ui.TagList.addItem(new_tag)
                    self.ui.tag_lineEdit.clear()
        else:
            new_tag = self.ui.tag_lineEdit_2.text().strip()
            if new_tag:
                if self.tags_manager.add_tag(self.type_id, new_tag, tag_area):
                    self.ui.TagList_2.addItem(new_tag)
                    self.ui.tag_lineEdit_2.clear()
        
                
    def _delete_tag(self, tag_area):
        """Удаляет выбранный тег"""
        if tag_area == 'name_tags':
            selected = self.ui.TagList.currentItem()
            if selected:
                tag_to_remove = selected.text()
                if self.tags_manager.remove_tag(self.type_id, tag_to_remove, tag_area):
                    self.ui.TagList.takeItem(self.ui.TagList.row(selected))
        else:
            selected = self.ui.TagList_2.currentItem()
            if selected:
                tag_to_remove = selected.text()
                if self.tags_manager.remove_tag(self.type_id, tag_to_remove, tag_area):
                    self.ui.TagList_2.takeItem(self.ui.TagList_2.row(selected))


class PEDSorterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ChoosePEDButton.clicked.connect(self.choose_ped)
        self.TAGS_FOR_LOCAL_ESTIMATE = ['локальная смета', 'лс', 'лc', 'cмета']
        self.TAGS_FOR_OBJECT_ESTIMATE = ['ОБЪЕКТНАЯ СМЕТА', 'ос']
        self.UNKNOWN = '?'
        self.BASE_NEW_NAME_FOR_LE = 'ЛС-??-01-БАЗ'
        self.TYPES_NAMES = {
            'local_estimate': '1. (локальная смета)',
            }
        self.logger = setup_logging()
        self.filenames = dict()
        self.ui.Table.cellDoubleClicked.connect(self.open_file_in_explorer)
        self.directory = ''
        self.ui.SearchButton.clicked.connect(self.traverse_directory)
        self.tags_manager = TagsManager()
        self._populate_files_list()
        self.ui.FilesList.itemDoubleClicked.connect(self._on_file_double_clicked)

    def _open_tags_window(self, type_id):
        """Открывает окно управления тегами"""
        self.tags_window = TagsWindow(type_id, self.tags_manager, self)
        self.tags_window.show()
    
    def _populate_files_list(self):
        """Заполняет FilesList всеми типами файлов из JSON"""
        self.ui.FilesList.clear()
        for type_id, type_data in self.tags_manager.tags_data.items():
            item_text = f"{type_id} - {type_data['type']}"
            item = QtWidgets.QListWidgetItem(item_text)
            item.setData(QtCore.Qt.UserRole, type_id)
            self.ui.FilesList.addItem(item)

    def _on_file_double_clicked(self, item):
        """Обработчик двойного клика по перечню файлов"""
        type_id = item.data(QtCore.Qt.UserRole)
        self._open_tags_window(type_id)

    def choose_ped(self):
        '''Обработчик кнопки "Выбрать ПСД".'''
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку ПСД")
        if directory:
            self.ui.DirectoryName.setText(directory)
            self.ui.SearchButton.setEnabled(True)
            self.directory = directory
        else:
            self.ui.SearchButton.setEnabled(False)

    def traverse_directory(self):
        '''Обходит выбранную директорию и все поддиректории.'''
        self.filenames = dict()
        for root, _, files in os.walk(self.directory):
            for filename in files:
                if os.path.basename(filename).startswith('~$'):
                    continue
                filepath = Path(root) / filename
                extension = filepath.suffix.lower()
                type = self.UNKNOWN
                new_name = self.UNKNOWN
                mask = self.UNKNOWN

                #выяснить, что за тип:
                for type_id, type_data in self.tags_manager.tags_data.items():
                    if self.ui.search_in_name_checkBox.isChecked():
                        file_parts = re.split(r'[_\-. ]+', filename.lower())
                        if any(tag.lower() in file_parts for tag in type_data["name_tags"]): #распознавание тэгов в имени
                            type = type_data["type"]
                            mask = type_data["mask"]
                            break
                    if self.ui.search_in_file_checkBox.isChecked():
                        if extension in ['.xls', '.xlsx']:
                            presence_tags_in_file = self.check_if_tags_in_file(type_data["internal_tags"], filepath)
                            if presence_tags_in_file:
                                self.logger.debug(f'обнаружен тэг "{presence_tags_in_file}"в файле: {filename}')
                                type = type_data["type"]
                                mask = type_data["mask"]
                                break
                if extension in ['.xls', '.xlsx']:
                    if type == 'Локальная смета':
                        new_name = self.create_name_for_local_estimate(filepath, filename)
                    if type == 'Объектная смета':
                        new_name = self.create_name_for_object_estimate(filepath, filename)
                    if type == 'Сводный сметный расчет':
                        new_name = self.create_name_for_summary_estimate(filepath, filename)

                self.filenames[filename] = { # ДОБАВИТЬ СЮДА БУРДУ ТИПА "ПАКЕТ" ?
                    'type': type,
                    'new_name': new_name,
                    'mask': mask,
                    'extension': extension,
                    'filepath': filepath
                    }
        self.share_info_from_xls_to_duplicates()
        self.populate_table()

    def check_if_tags_in_file(self, internal_tags, filepath):
        """Проверяет, встречаются ли тэги в файле"""
        file = self.read_xls_xlsx_file(filepath)
        if file is not None and not file.empty:
            for i in range(len(file)):
                row_data = ''.join([str(x).lower() for x in file.iloc[i].values.tolist() if pd.notna(x)])
                for tag in internal_tags:
                    if tag.lower() in row_data:
                        return row_data
        return False

    def share_info_from_xls_to_duplicates(self):
        """Если находятся файлы одинакового имени, но разного расширения, эта функция
        передаст инфу о типе и новом имени от xls файла тёскам других расширений"""
        for filename, data in self.filenames.items():
            ext = data['extension']
            if ext in ['.xls', '.xlsx']:
                name_without_ext = os.path.splitext(filename)[0]
                for filename2, data2 in self.filenames.items():
                    if os.path.splitext(filename2)[0] == name_without_ext and filename != filename2:
                        data2['new_name'] = data['new_name']
                        data2['type'] = data['type']
                        data2['mask'] = data['mask']

    def read_xls_xlsx_file(self, filepath):
        if os.path.basename(filepath).startswith('~$'):
            return None
        if not os.path.exists(filepath):
            self.logger.error(f'Файл не существует: {filepath}')
            return None
        try:
            if str(filepath).lower().endswith('.xlsx'):
                engine = 'openpyxl'
            elif str(filepath).lower().endswith('.xls'):
                engine = 'xlrd'
            else:
                self.logger.error(f"Неизвестный формат файла: {filepath}")
                return None
            opened_file = pd.read_excel(filepath, engine=engine, header=None)
        except Exception as e:
            self.logger.error(f"Ошибка чтения файла {filepath}: {str(e)}")
            return None
        return opened_file

    def create_name_for_local_estimate(self, filepath, filename):
        """Создает новое имя для локальной сметы: """
        TARGET_TEXT = ['локальн', 'смета', 'сметный']
        ESTIMATE_NUMBER_UNKNOWN = '??-??-??'
        estimate_number = ESTIMATE_NUMBER_UNKNOWN
        DEFAULT_VERSION = 'БАЗ'
        version = DEFAULT_VERSION
        file = self.read_xls_xlsx_file(filepath)
        lines_to_chek = 20 #в скольких первых строках искать совпадения. весь файл = len(file)
        if file is not None and not file.empty:
            for i in range(lines_to_chek):
                row_data = ''.join([str(x).lower() for x in file.iloc[i].values.tolist() if pd.notna(x)])
                for tag in list(map(lambda x: x.lower(), TARGET_TEXT)):
                    if tag in row_data:
                        if '№' in row_data:
                            number = row_data.split('№')[-1].strip()
                            if re.search(r'^\d{2}-\d{2}(?:-\d{2})?$', number):
                                estimate_number = number
                                break
        return f'ЛС-{estimate_number}-{version}-(ex. {filename[:10]}..)'

    def create_name_for_object_estimate(self, filepath, filename):
        """Создает новое имя для объектной сметы: """
        TARGET_TEXT = ['объектн', 'смета', 'сметный']
        ESTIMATE_NUMBER_UNKNOWN = '??-??'
        estimate_number = ESTIMATE_NUMBER_UNKNOWN
        DEFAULT_VERSION = 'БАЗ'
        version = DEFAULT_VERSION
        file = self.read_xls_xlsx_file(filepath)
        lines_to_chek = 20 #в скольких первых строках искать совпадения. весь файл = len(file)
        if file is not None and not file.empty:
            for i in range(lines_to_chek):
                row_data = ''.join([str(x).lower() for x in file.iloc[i].values.tolist() if pd.notna(x)])
                for tag in list(map(lambda x: x.lower(), TARGET_TEXT)):
                    if tag in row_data:
                        if '№' in row_data:
                            number = row_data.split('№')[-1].strip()
                            temp = re.search(r'^\d{2}(?:-\d{2})?$', number)
                            if temp:
                                self.logger.debug(f'!!!!!!!!!{number}!!!!!!!!!! {temp}')
                                estimate_number = number
                                break
        return f'ОС-{estimate_number}-{version}-(ex. {filename[:10]}..)'

    def create_name_for_summary_estimate(self, filepath, filename):
        """Создает новое имя для сводного сметного расчета: """
        TARGET_TEXT = ['сводн', 'смета', 'сметный']
        ESTIMATE_NUMBER_UNKNOWN = '??'
        estimate_number = ESTIMATE_NUMBER_UNKNOWN
        DEFAULT_VERSION = 'БАЗ'
        version = DEFAULT_VERSION
        file = self.read_xls_xlsx_file(filepath)
        lines_to_chek = 20 #в скольких первых строках искать совпадения. весь файл = len(file)
        if file is not None and not file.empty:
            for i in range(lines_to_chek):
                row_data = ''.join([str(x).lower() for x in file.iloc[i].values.tolist() if pd.notna(x)])
                for tag in list(map(lambda x: x.lower(), TARGET_TEXT)):
                    if tag in row_data:
                        if '№' in row_data:
                            number = row_data.split('№')[-1].strip()
                            if re.search(r'^\d{2}$', number):
                                estimate_number = number
                                break
        return f'ОС-{estimate_number}-{version}-(ex. {filename[:10]}..)'

    def populate_table(self):
        '''Заполняет таблицу найденными файлами.'''
        self.ui.Table.setRowCount(len(self.filenames))
        for row, (filename, data) in enumerate(self.filenames.items()):
            self.ui.Table.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))
            self.ui.Table.setItem(row, 1, QtWidgets.QTableWidgetItem(data['type']))
            self.ui.Table.setItem(row, 2, QtWidgets.QTableWidgetItem(data['mask']))
            self.ui.Table.setItem(row, 3, QtWidgets.QTableWidgetItem(data['new_name'] + data['extension']))

            if data['type'] != self.UNKNOWN:
                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Checked)
                self.ui.Table.setItem(row, 4, checkbox_item)
            else:
                self.ui.Table.setItem(row, 4, QtWidgets.QTableWidgetItem(''))
            
            if data['type'] == '?': #ЦВЕТА!
                color = QtGui.QColor(236, 200, 174)
                for col in range(self.ui.Table.columnCount()):
                    self.ui.Table.item(row, col).setBackground(color)
            else: #ЦВЕТА!
                color = QtGui.QColor(221, 255, 217)
                for col in range(self.ui.Table.columnCount()):
                    self.ui.Table.item(row, col).setBackground(color)

    def open_file_in_explorer(self, row, column):
        '''Открывает файл в проводнике при двойном клике на имя файла (колонка 0)'''
        if column == 0:
            filename_item = self.ui.Table.item(row, column)
            if filename_item:
                file_path = self.filenames[filename_item.text()]['filepath']
            if os.path.exists(file_path):
                if sys.platform == 'win32':
                    import subprocess
                    subprocess.Popen(f'explorer /select,"{os.path.abspath(file_path)}"')
            else:
                QtWidgets.QMessageBox.warning(self, 'Ошибка', f'Файл не найден:\n{file_path}')


def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"ped_sorter_{datetime.now().strftime('%Y%m%d')}.log")

    logger = logging.getLogger("PEDSorter")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def main():
    
    app = QtWidgets.QApplication(sys.argv)
    window = PEDSorterApp() 
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


