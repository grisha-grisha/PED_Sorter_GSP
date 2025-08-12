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
        self.tags_file = self.exec_dir / 'name_tags_base1.json'
        self.tags_data = self._load_tags()
        self.tags_data = self._load_tags()
        self.logger = setup_logging()

    def _load_tags(self):
        """Загружает теги из файла или создает новый с дефолтными значениями"""
        default_tags = {
                "1": {
                    "name": "Локальная смета",
                    "tags": ["локальная смета", "лс"],
                    "mask": "ЛС-ОС-ПН-ВЕРНН-КОММ"
                },
                "2": {
                    "name": "Объектная смета",
                    "tags": ["объектная смета", "ос"],
                    "mask": "ОС-ГС-ПН-ВЕРНН-КОММ"
                },
                "3": {
                    "name": "Сводный сметный расчет",
                    "tags": ["cводный сметный расчет", "расчет", "сср"],
                    "mask": "ССР-ПН-ВЕРНН-КОММ"
                },
                "4": {
                    "name": "Сводный реестр сметной документации",
                    "tags": ["cводный реестр сметной документации", "реестр", "срсд", "рд"],
                    "mask": "СРСД-ВЕРНН-КОММ"
                },
                "5": {
                    "name": "Сметные расчеты на отдельные виды затрат ",
                    "tags": ["cметные расчеты на отдельные виды затрат", "сровз"],
                    "mask": "СРОВЗ-ВЕРНН-КОММ"
                },
                "6": {
                    "name": "Сравнительная таблица изменения стоимости МТР по договору подряда (Форма 1.3)",
                    "tags": ["таблица", "МТР", "форма1.3"],
                    "mask": "ФОРМА1.3-ВЕРНН-КОММ"
                },
                "7": {
                    "name": "Расчеты на прочие затраты",
                    "tags": ["расчеты на прочие затраты", "прочие затраты", "рпз"],
                    "mask": "ПРОЧ-ТИП-ВЕРНН-КОММ"
                },
                "7.1": {
                    "name": "Перевозка",
                    "tags": ["перевозка"],
                    "mask": "ПРОЧ-Перевозка-ВЕРНН-КОММ"
                },
                "7.2": {
                    "name": "Командировочные расходы",
                    "tags": ["командировочные расходы"],
                    "mask": "ПРОЧ-Командировочные-ВЕРНН-КОММ"
                },
                "7.3": {
                    "name": "Перебазировка",
                    "tags": ["перебазировка"],
                    "mask": "ПРОЧ-Перебазировка-ВЕРНН-КОММ"
                },
                "7.4": {
                    "name": "Затраты на охрану труда",
                    "tags": ["охрана труда"],
                    "mask": "ПРОЧ-ОхранаТруда-ВЕРНН-КОММ"
                },
                "7.5": {
                    "name": "Затраты на проведение пусконаладочных работ (ПНР)",
                    "tags": ["пнр", "затраты на пнр"],
                    "mask": "ПРОЧ-ПНР-ВЕРНН-КОММ"
                },
                "7.6": {
                    "name": "Устройство дорог",
                    "tags": ["устройство дорог"],
                    "mask": "ПРОЧ-УстройствоДорог-ВЕРНН-КОММ"
                },
                "7.7": {
                    "name": "Дополнительные затраты при производстве работ в зимнее время",
                    "tags": ["зу"],
                    "mask": "ПРОЧ-ЗУ-ВЕРНН-КОММ"
                },
                "7.8": {
                    "name": "Утилизация отходов",
                    "tags": ["утилизация отходов", "утилизация"],
                    "mask": "ПРОЧ-УтилизацияОтходов-ВЕРНН-КОММ"
                },
                "7.9": {
                    "name": "Плата за негативное воздействие на окружающую среду (НВОС)",
                    "tags": ["негативное", "воздействие", "окружающую", "нвос"],
                    "mask": "ПРОЧ-НВОС-ВЕРНН-КОММ"
                },
                "7.10": {
                    "name": "Транспортировка",
                    "tags": ["транспортировка"],
                    "mask": "ПРОЧ-Транспортировка-ВЕРНН-КОММ"
                },
                "7.11": {
                    "name": "Плавсредства",
                    "tags": ["плавсредства"],
                    "mask": "ПРОЧ-Плавсредства-ВЕРНН-КОММ"
                },
                "7.12": {
                    "name": "Затраты на мониторинг компонентов окружающей среды (ПЭМ)",
                    "tags": ["пэм", "мониторинг", "компонентов"],
                    "mask": "ПРОЧ-ПЭМ-ВЕРНН-КОММ"
                },
                "8": {
                    "name": "Подтверждающие документы",
                    "tags": ["подтв"],
                    "mask": "ПОДТВ-ТИП-ТИППРОЧ-ПН-ВЕРНН-КОММ"
                },
                "8.1": {
                    "name": "Ведомость объемов работ",
                    "tags": ["ведомость объемов работ"],
                    "mask": "ПОДТВ-ВОР-ПН-ВЕРНН-КОММ"
                },
                "8.2": {
                    "name": "Дефектная ведомость",
                    "tags": ["дефектная ведомость", "ДВ", "ВД"],
                    "mask": "ПОДТВ-ДВ-ПН-ВЕРНН-КОММ"
                },
                "8.3": {
                    "name": "Коммерческое предложение",
                    "tags": ["коммерческое", "ткп", "кп"],
                    "mask": "ПОДТВ-КП-ПН-ВЕРНН-КОММ"
                },
                "8.4": {
                    "name": "Транспортная схема",
                    "tags": ["тс", "транспортная схема"],
                    "mask": "ПОДТВ-ТС-ПН-ВЕРНН-КОММ"
                },
                "8.5": {
                    "name": "Обоснование к расчету прочих затрат",
                    "tags": ["обоснование", "", ""],
                    "mask": "ПОДТВ-ОбоснованиеПрочих-ТИППРОЧ-ПН-ВЕРНН-КОММ"
                },
                "8.6": {
                    "name": "Конъюнктурный анализ",
                    "tags": ["конъюнктурный", "ка"],
                    "mask": "ПОДТВ-КА-ПН-ВЕРНН-КОММ"
                }
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

    def add_tag(self, type_id, new_tag):
        """Добавляет новый тег для типа"""
        type_id = str(type_id)
        if type_id not in self.tags_data:
            return False
        
        if new_tag not in self.tags_data[type_id]["tags"]:
            self.tags_data[type_id]["tags"].append(new_tag)
            self._save_tags(self.tags_data)
            return True
        return False

    def remove_tag(self, type_id, tag_to_remove):
        """Удаляет тег у указанного типа"""
        type_id = str(type_id)
        if type_id in self.tags_data and tag_to_remove in self.tags_data[type_id]["tags"]:
            self.tags_data[type_id]["tags"].remove(tag_to_remove)
            self._save_tags(self.tags_data)
            return True
        return False


class TagsWindow(QtWidgets.QMainWindow):
    def __init__(self, type_id, tags_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_TagsWindow()
        self.ui.setupUi(self)
        self.type_id = str(type_id)
        self.tags_manager = tags_manager
        self._setup_ui()
        self._connect_signals()
        
    def _setup_ui(self):
        """Заполняет окно данными"""
        type_data = self.tags_manager.get_type_data(self.type_id)
        if type_data:
            self.ui.type_label.setText(type_data["name"])
            self.ui.TagList.addItems(type_data["tags"])
        
    def _connect_signals(self):
        """Подключает сигналы кнопок"""
        self.ui.add_tag.clicked.connect(self._add_tag)
        self.ui.delete_tag.clicked.connect(self._delete_tag)
        self.ui.lineEdit.returnPressed.connect(self._add_tag)
        
    def _add_tag(self):
        """Добавляет новый тег"""
        new_tag = self.ui.lineEdit.text().strip()
        if new_tag:
            if self.tags_manager.add_tag(self.type_id, new_tag):
                self.ui.TagList.addItem(new_tag)
                self.ui.lineEdit.clear()
                
    def _delete_tag(self):
        """Удаляет выбранный тег"""
        selected = self.ui.TagList.currentItem()
        if selected:
            tag_to_remove = selected.text()
            if self.tags_manager.remove_tag(self.type_id, tag_to_remove):
                self.ui.TagList.takeItem(self.ui.TagList.row(selected))


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
        self.filenames = dict() #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! обнуляй список при выборе новой дирректории!!!!!!!!!!!!!!!!!!!!
        self.tags_manager = TagsManager()
        self._setup_tag_buttons()
        self.ui.Table.cellDoubleClicked.connect(self.open_file_in_explorer)

    def _setup_tag_buttons(self):
        """Связывает кнопки тегов с обработчиками"""
        self.ui.tagButton_1.clicked.connect(
            lambda: self._open_tags_window('1')
        )
        self.ui.tagButton_2.clicked.connect(
            lambda: self._open_tags_window('2')
        )
    def _open_tags_window(self, type_id):
        """Открывает окно управления тегами"""
        self.tags_window = TagsWindow(type_id, self.tags_manager, self)
        self.tags_window.show()
    
    def choose_ped(self):
        '''Обработчик кнопки "Выбрать ПСД".'''
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку ПСД")
        if directory:
            self.ui.DirectoryName.setText(directory)
            self.ui.files_frame.setEnabled(True)
            self.ui.SearchButton.setEnabled(True)
            self.ui.SearchButton.clicked.connect(lambda: self.traverse_directory(directory))
        else:
            self.ui.files_frame.setEnabled(False)
            self.ui.SearchButton.setEnabled(False)
    
    def traverse_directory(self, directory):
        '''Обходит выбранную директорию и все поддиректории.'''
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = Path(root) / filename
                extension = filepath.suffix.lower()
                type = self.UNKNOWN
                new_name = self.UNKNOWN
                mask = self.UNKNOWN
                for type_id, type_data in self.tags_manager.tags_data.items():
                    if any(tag.lower() in filename.lower() for tag in type_data["tags"]):
                        file_type = type_data["name"]
                        mask = type_data.get("mask", self.UNKNOWN)
                    if type_id == "1" and extension in ['.xls', '.xlsx']:
                        new_name = self.create_name_for_local_estimate(filepath)
                    else:
                        new_name = f"{mask}{extension}"
                    break

                self.filenames[filename] = {
                    'type': type,
                    'new_name': new_name,
                    'mask': mask,
                    'extension': extension,
                    'filepath': filepath
                    }
        self.populate_table()

    def create_name_for_local_estimate(self, filepath):
        TARGET_TEXT = ['локальная', 'смета']
        DEFECTIVE_TEXT = ['', ' ']
        ESTIMATE_NUMBER_UNKNOWN = '??-??'
        estimate_number = ESTIMATE_NUMBER_UNKNOWN
        sequence_number = '01'
        version = 'БАЗ'
        if os.path.basename(filepath).startswith('~$'):
            return self.BASE_NEW_NAME_FOR_LE
            
        if not os.path.exists(filepath):
            self.logger.error(f"Файл не существует: {filepath}")
            return self.BASE_NEW_NAME_FOR_LE
            
        try:
            if str(filepath).lower().endswith('.xlsx'):
                engine = 'openpyxl'
            elif str(filepath).lower().endswith('.xls'):
                engine = 'xlrd'
            else:
                self.logger.error(f"Неизвестный формат файла: {filepath}")
                return self.BASE_NEW_NAME_FOR_LE
            le_file = pd.read_excel(filepath, engine=engine, header=None)

        except Exception as e:
            self.logger.error(f"Ошибка чтения файла {filepath}: {str(e)}")
            return self.BASE_NEW_NAME_FOR_LE
        
        for i in range(len(le_file)):
            row_data = ''.join([str(x).lower() for x in le_file.iloc[i].values.tolist() if pd.notna(x)])
            for tag in TARGET_TEXT:
                if tag in row_data:
                    if '№' in row_data:
                        estimate_number = row_data.split('№')[-1].strip()
                        if estimate_number in DEFECTIVE_TEXT:
                            estimate_number = ESTIMATE_NUMBER_UNKNOWN
                        break
        return f'ЛС-{estimate_number}-{sequence_number}-{version}'

    def check_if_local_estimate(self, filename):
        '''Проверка тэгов локальной сметы в названии'''
        type_data = self.tags_manager.get_type_data("1")
        if not type_data:
            return False
        filename_lower = filename.lower()
        return any(tag.lower() in filename_lower for tag in type_data["tags"])

    def populate_table(self):
        '''Заполняет таблицу найденными файлами.'''
        self.ui.Table.setRowCount(len(self.filenames))
        for row, (filename, data) in enumerate(self.filenames.items()):

            if data['type'] == self.TYPES_NAMES['local_estimate']:
                if data['new_name'] == self.BASE_NEW_NAME_FOR_LE:
                    name_without_ext = os.path.splitext(filename)[0]
                    if name_without_ext + '.xls' in self.filenames.keys():
                        data['new_name'] = self.filenames[name_without_ext + '.xls']['new_name']
                    if name_without_ext + '.xlsx' in self.filenames.keys():
                        data['new_name'] = self.filenames[name_without_ext + '.xlsx']['new_name']

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
            
            if data['type'] == self.TYPES_NAMES['local_estimate']:
                color = QtGui.QColor(230, 255, 230)
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


