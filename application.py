import logging
from struct import unpack_from, pack_into

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from constants import INITIAL_GAP, BLOCK_SIZE, BASIC_STATS, FLOAT_FORMAT, INT_FORMAT, END_POINTER

import editor


class EditorApp(QtWidgets.QMainWindow, editor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger('Editor Patapon file')
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.openFileButton.clicked.connect(self.open_file)
        self.exitButton.clicked.connect(self.exit_app)
        self.saveFileButton_2.clicked.connect(self.save_file)
        self.comboBox.currentTextChanged.connect(self.process_item)
        self._file_content = None
        self._all_items = []
        self._file_name = None
        self.item_model = QStandardItemModel(self.comboBox)
        self._only_int = QIntValidator()
        self._only_float = QDoubleValidator()
        self.set_validators()
        self.set_processor()

    def save_file(self):
        self._logger.debug('Saving file')
        if self._file_name is None:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Файл не загружен, нечего сохранять!')
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
        else:

            try:
                with open(self._file_name, 'wb') as data_file:
                    data_file.write(self._file_content)
            except Exception:
                self._logger.exception('Write error')

    def process_edited_item(self, text):
        line_edit = self.sender()
        object_name = line_edit.objectName()
        current_stat = next(item for item in BASIC_STATS if item[1] == object_name)
        current_stat_offset = current_stat[0]
        current_stat_format = current_stat[2]
        current_item_name = self.comboBox.currentText()
        current_item = next(item for item in self._all_items if item[0] == current_item_name)
        current_block_offset = current_item[1]
        self._logger.debug('Changed value %s for %s item %s', text, object_name, current_item)
        if current_stat_format == FLOAT_FORMAT:
            value = float(text.replace(',', '.'))
        elif current_stat_format == INT_FORMAT:
            value = float(text.replace(',', '.'))
        else:
            raise ValueError('Неподдерживаемый формат %s !', current_stat_format)
        pack_into(current_stat_format,
                  self._file_content,
                  current_block_offset + current_stat_offset,
                  value)

    def set_processor(self):
        for element in BASIC_STATS:
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                line_edit.textEdited.connect(self.process_edited_item)

    def open_file(self):
        self._logger.debug('Opening file')
        try:
            input_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл')
            self._file_name = input_file[0]
            self._logger.info('Input file: %s', self._file_name)
            with open(self._file_name, 'rb') as data_file:
                self._file_content = bytearray(data_file.read())
            self.bck = self._file_content.copy()
            file_length = len(self._file_content)
            self._logger.info('Read %s bytes', file_length)
            if self._file_content[0:6] != bytearray.fromhex('5947465f4746'):
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Неопознанный формат файла!')
                error_dialog.setWindowTitle("Ошибка")
                error_dialog.exec_()
                raise ValueError('Неопознанный формат файла!')
            self.fileName.setText(input_file[0])
            self.get_all_names()
            self.centralwidget.setWindowTitle(f'Patapon Resource file editor: {input_file[0]}')
        except Exception:
            self._logger.exception('При открытии файла произошла ошибка')
            self._file_content = None
            self._all_items = []
            self.item_model = QStandardItemModel(self.comboBox)
            self.fileName.setText('')

    def exit_app(self):
        self._logger.info('Exiting')
        QtCore.QCoreApplication.instance().quit()

    def get_all_names(self):
        pointer: int = INITIAL_GAP
        loaded_quantity: int = 0
        self._all_items = []
        self.item_model = QStandardItemModel(self.comboBox)
        while pointer < END_POINTER:
            weapon_name = self._file_content[pointer: pointer + 0x10].decode('utf-8').strip('\x00')
            self._all_items.append((weapon_name, pointer))
            item = QStandardItem(weapon_name)
            self.item_model.appendRow(item)
            pointer += BLOCK_SIZE
            loaded_quantity += 1
        self._logger.debug(self._all_items)
        self.comboBox.setModel(self.item_model)
        self.loadedCount.display(loaded_quantity)

    def process_item(self, text):
        try:
            self.set_values_editable()
            offset = next(item for item in self._all_items if item[0] == text)[1]
            block = self._file_content[offset:offset + BLOCK_SIZE]
            self._logger.debug(block)
            for element in BASIC_STATS:
                value = unpack_from(element[2], block, element[0])[0]
                self._logger.debug('Value: %s', value)
                line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
                if line_edit is not None:
                    line_edit.setText(str(value).replace('.', ','))

        except Exception:
            self._logger.exception('При загрузке данных элемента произошла ошибка')
            self.set_values_readonly()

    def set_validators(self):
        self._logger.debug('SetValidators')
        for element in BASIC_STATS:
            self._logger.debug('x00: %s', element)
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                if element[2] == FLOAT_FORMAT:
                    self._logger.debug('x01: %s', element)
                    line_edit.setValidator(self._only_float)
                elif element[2] == INT_FORMAT:
                    line_edit.setValidator(self._only_int)

    def set_values_readonly(self):
        for element in BASIC_STATS:
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                line_edit.setReadOnly(True)

    def set_values_editable(self):
        for element in BASIC_STATS:
            line_edit = self.findChild(QtWidgets.QLineEdit, element[1])
            if line_edit is not None:
                line_edit.setReadOnly(False)
