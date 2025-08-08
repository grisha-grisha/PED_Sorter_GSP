import sys
import os
from pathlib import Path

import pandas as pd
from PySide6 import QtWidgets, QtGui, QtCore

from PED_design import Ui_MainWindow


class PEDSorterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ChoosePEDButton.clicked.connect(self.choose_ped)
        self.TAGS_FOR_LOCAL_ESTIMATE = ['локальная смета', 'лс', 'cмета']
        self.TAGS_FOR_OBJECT_ESTIMATE = ['ОБЪЕКТНАЯ СМЕТА', 'ос']
        self.UNKNOWN = '?'
        self.BASE_NEW_NAME_FOR_LE = 'ЛС-??-01-БАЗ'
        self.TYPES_NAMES = {
            'local_estimate': '1. (локальная смета)',
            }
        
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
        filenames = dict()
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = Path(root) / filename
                extension = filepath.suffix.lower()
                type = self.UNKNOWN
                new_name = self.UNKNOWN
                mask = self.UNKNOWN
                if self.ui.checkBox_1.isChecked():
                    if self.check_if_local_estimate(filename):
                        type = self.TYPES_NAMES['local_estimate']
                        new_name = self.BASE_NEW_NAME_FOR_LE
                        mask = 'ЛС-ОС-ПН-ВЕРРНН-КОММ'
                        if extension in ['.xls', '.xlsx']:
                            new_name = self.create_name_for_local_estimate(filepath)

                filenames[filename] = {
                    'type': type,
                    'new_name': new_name,
                    'mask': mask,
                    'extension': extension
                    }
        self.populate_table(filenames)

    def create_name_for_local_estimate(self, filepath):
        le_file = pd.read_excel(filepath, engine='openpyxl', header=None)
        TARGET_TEXT = ['локальная', 'смета']
        DEFECTIVE_TEXT = ['', ' ']
        ESTIMATE_NUMBER_UNKNOWN = '??-??'
        estimate_number = ESTIMATE_NUMBER_UNKNOWN
        sequence_number = '01'
        version = 'БАЗ'
        if os.path.basename(filepath).startswith('~$'):
            return self.BASE_NEW_NAME_FOR_LE
            
        if not os.path.exists(filepath):
            print(f"Файл не существует: {filepath}")
            return self.BASE_NEW_NAME_FOR_LE
            
        try:
            le_file = pd.read_excel(filepath, engine='openpyxl', header=None)
        except Exception as e:
            print(f"Ошибка чтения файла {filepath}: {str(e)}")
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
        for tag in self.TAGS_FOR_LOCAL_ESTIMATE:
            if tag.lower() in filename.lower():
                return True

    def populate_table(self, filenames):
        '''Заполняет таблицу найденными файлами.'''
        self.ui.Table.setRowCount(len(filenames))
        for row, (filename, data) in enumerate(filenames.items()):

            if data['type'] == self.TYPES_NAMES['local_estimate']:
                if data['new_name'] == self.BASE_NEW_NAME_FOR_LE:
                    name_without_ext = os.path.splitext(filename)[0]
                    if name_without_ext + '.xls' in filenames.keys():
                        data['new_name'] = filenames[name_without_ext + '.xls']['new_name']
                    if name_without_ext + '.xlsx' in filenames.keys():
                        data['new_name'] = filenames[name_without_ext + '.xlsx']['new_name']

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
        
            


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PEDSorterApp() 
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
