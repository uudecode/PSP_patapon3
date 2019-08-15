import logging
from struct import unpack_from

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from constants import INITIAL_GAP, BLOCK_SIZE, BASIC_STATS, FLOAT_FORMAT, INT_FORMAT

import editor


class EditorApp(QtWidgets.QMainWindow, editor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger('Editor Patapon file')
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.openFileButton.clicked.connect(self.open_file)
        self.exitButton.clicked.connect(self.exit_app)
        self.listItems.clicked.connect(self.process_item)
        self._file_content = None
        self._all_items = []
        self.item_model = QStandardItemModel(self.listItems)
        self._only_int = QIntValidator()
        self._only_float = QDoubleValidator()
        self.set_validators()

    def open_file(self):
        self._logger.debug('Opening file')
        try:
            input_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл')
            self._logger.info('Input file: %s', input_file[0])
            with open(input_file[0], 'rb') as data_file:
                self._file_content = bytearray(data_file.read())
            file_length = len(self._file_content)
            self._logger.info('Read %s bytes', file_length)
            if self._file_content[0:6] != bytearray.fromhex('5947465f4746'):
                raise ValueError('Неопознанный формат файла!')
            self.fileName.setText(input_file[0])
            self.get_all_names()
            self.centralwidget.setWindowTitle(f'Patapon Resource file editor: {input_file[0]}')
        except Exception:
            self._logger.exception('При открытии файла произошла ошибка')
            self._file_content = None
            self._all_items = []
            self.item_model = QStandardItemModel(self.listItems)
            self.fileName.setText('')

    def exit_app(self):
        self._logger.info('Exiting')
        QtCore.QCoreApplication.instance().quit()

    def get_all_names(self):
        pointer: int = INITIAL_GAP
        self._all_items = []
        self.item_model = QStandardItemModel(self.listItems)
        while pointer < len(self._file_content):
            weapon_name = self._file_content[pointer: pointer + 0x10].decode('utf-8')
            self._all_items.append((pointer, weapon_name))
            item = QStandardItem(weapon_name)
            self.item_model.appendRow(item)
            pointer += BLOCK_SIZE
        self._logger.debug(self._all_items)
        self.listItems.setModel(self.item_model)

    def process_item(self, index):
        self._logger.debug(self._all_items[index.row()])
        try:
            self.set_values_editable()
            offset = self._all_items[index.row()][0]
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
