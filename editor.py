# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1158, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listItems = QtWidgets.QListView(self.centralwidget)
        self.listItems.setGeometry(QtCore.QRect(938, 20, 191, 481))
        self.listItems.setObjectName("listItems")
        self.HPBase_label = QtWidgets.QLabel(self.centralwidget)
        self.HPBase_label.setGeometry(QtCore.QRect(30, 40, 111, 16))
        self.HPBase_label.setObjectName("HPBase_label")
        self.MinDMGScaling = QtWidgets.QLineEdit(self.centralwidget)
        self.MinDMGScaling.setGeometry(QtCore.QRect(129, 190, 110, 20))
        self.MinDMGScaling.setObjectName("MinDMGScaling")
        self.MinDMGScaling_label = QtWidgets.QLabel(self.centralwidget)
        self.MinDMGScaling_label.setGeometry(QtCore.QRect(30, 190, 77, 13))
        self.MinDMGScaling_label.setObjectName("MinDMGScaling_label")
        self.FeverSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.FeverSpeed.setGeometry(QtCore.QRect(129, 100, 110, 20))
        self.FeverSpeed.setObjectName("FeverSpeed")
        self.HPScaling_label = QtWidgets.QLabel(self.centralwidget)
        self.HPScaling_label.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.HPScaling_label.setObjectName("HPScaling_label")
        self.MinDMG_label = QtWidgets.QLabel(self.centralwidget)
        self.MinDMG_label.setGeometry(QtCore.QRect(30, 160, 71, 21))
        self.MinDMG_label.setObjectName("MinDMG_label")
        self.SprintSpeed_label = QtWidgets.QLabel(self.centralwidget)
        self.SprintSpeed_label.setGeometry(QtCore.QRect(30, 130, 81, 16))
        self.SprintSpeed_label.setObjectName("SprintSpeed_label")
        self.labelFeverSpeed_label = QtWidgets.QLabel(self.centralwidget)
        self.labelFeverSpeed_label.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.labelFeverSpeed_label.setObjectName("labelFeverSpeed_label")
        self.MaxDMG_label = QtWidgets.QLabel(self.centralwidget)
        self.MaxDMG_label.setGeometry(QtCore.QRect(30, 220, 61, 20))
        self.MaxDMG_label.setObjectName("MaxDMG_label")
        self.HPScaling = QtWidgets.QLineEdit(self.centralwidget)
        self.HPScaling.setGeometry(QtCore.QRect(129, 70, 110, 20))
        self.HPScaling.setReadOnly(True)
        self.HPScaling.setObjectName("HPScaling")
        self.MinDMG = QtWidgets.QLineEdit(self.centralwidget)
        self.MinDMG.setGeometry(QtCore.QRect(129, 160, 110, 21))
        self.MinDMG.setObjectName("MinDMG")
        self.MaxDMG = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxDMG.setGeometry(QtCore.QRect(130, 220, 110, 20))
        self.MaxDMG.setObjectName("MaxDMG")
        self.SprintSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.SprintSpeed.setGeometry(QtCore.QRect(129, 130, 110, 20))
        self.SprintSpeed.setObjectName("SprintSpeed")
        self.HPBase = QtWidgets.QLineEdit(self.centralwidget)
        self.HPBase.setGeometry(QtCore.QRect(129, 40, 110, 20))
        self.HPBase.setReadOnly(True)
        self.HPBase.setObjectName("HPBase")
        self.MaxDMGScaling_label = QtWidgets.QLabel(self.centralwidget)
        self.MaxDMGScaling_label.setGeometry(QtCore.QRect(30, 250, 101, 20))
        self.MaxDMGScaling_label.setObjectName("MaxDMGScaling_label")
        self.MaxDMGScaling = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxDMGScaling.setGeometry(QtCore.QRect(130, 250, 110, 20))
        self.MaxDMGScaling.setObjectName("MaxDMGScaling")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 271, 601))
        self.groupBox.setObjectName("groupBox")
        self.PowerScaling_label = QtWidgets.QLabel(self.groupBox)
        self.PowerScaling_label.setGeometry(QtCore.QRect(10, 300, 91, 21))
        self.PowerScaling_label.setObjectName("PowerScaling_label")
        self.PowerScaling = QtWidgets.QLineEdit(self.groupBox)
        self.PowerScaling.setGeometry(QtCore.QRect(110, 300, 111, 20))
        self.PowerScaling.setText("")
        self.PowerScaling.setObjectName("PowerScaling")
        self.ShieldBreak = QtWidgets.QLineEdit(self.groupBox)
        self.ShieldBreak.setGeometry(QtCore.QRect(110, 330, 111, 20))
        self.ShieldBreak.setObjectName("ShieldBreak")
        self.ShieldBreak_label = QtWidgets.QLabel(self.groupBox)
        self.ShieldBreak_label.setGeometry(QtCore.QRect(10, 330, 91, 21))
        self.ShieldBreak_label.setObjectName("ShieldBreak_label")
        self.ShieldBreakScaling_label = QtWidgets.QLabel(self.groupBox)
        self.ShieldBreakScaling_label.setGeometry(QtCore.QRect(10, 360, 101, 21))
        self.ShieldBreakScaling_label.setObjectName("ShieldBreakScaling_label")
        self.Power_label = QtWidgets.QLabel(self.groupBox)
        self.Power_label.setGeometry(QtCore.QRect(10, 270, 91, 20))
        self.Power_label.setObjectName("Power_label")
        self.ShieldBreakScaling = QtWidgets.QLineEdit(self.groupBox)
        self.ShieldBreakScaling.setGeometry(QtCore.QRect(110, 360, 111, 20))
        self.ShieldBreakScaling.setObjectName("ShieldBreakScaling")
        self.Power = QtWidgets.QLineEdit(self.groupBox)
        self.Power.setGeometry(QtCore.QRect(110, 270, 111, 20))
        self.Power.setObjectName("Power")
        self.Defense = QtWidgets.QLineEdit(self.groupBox)
        self.Defense.setGeometry(QtCore.QRect(110, 390, 111, 20))
        self.Defense.setObjectName("Defense")
        self.DefenseScaling = QtWidgets.QLineEdit(self.groupBox)
        self.DefenseScaling.setGeometry(QtCore.QRect(110, 420, 111, 20))
        self.DefenseScaling.setObjectName("DefenseScaling")
        self.Evasion = QtWidgets.QLineEdit(self.groupBox)
        self.Evasion.setGeometry(QtCore.QRect(110, 450, 111, 20))
        self.Evasion.setObjectName("Evasion")
        self.EvasionScaling = QtWidgets.QLineEdit(self.groupBox)
        self.EvasionScaling.setGeometry(QtCore.QRect(110, 480, 111, 20))
        self.EvasionScaling.setObjectName("EvasionScaling")
        self.Weight = QtWidgets.QLineEdit(self.groupBox)
        self.Weight.setGeometry(QtCore.QRect(110, 510, 111, 20))
        self.Weight.setObjectName("Weight")
        self.WeightScaling = QtWidgets.QLineEdit(self.groupBox)
        self.WeightScaling.setGeometry(QtCore.QRect(110, 540, 111, 20))
        self.WeightScaling.setObjectName("WeightScaling")
        self.Defense_label = QtWidgets.QLabel(self.groupBox)
        self.Defense_label.setGeometry(QtCore.QRect(10, 390, 101, 21))
        self.Defense_label.setObjectName("Defense_label")
        self.DefenseScaling_label = QtWidgets.QLabel(self.groupBox)
        self.DefenseScaling_label.setGeometry(QtCore.QRect(10, 420, 101, 21))
        self.DefenseScaling_label.setObjectName("DefenseScaling_label")
        self.Evasion_label = QtWidgets.QLabel(self.groupBox)
        self.Evasion_label.setGeometry(QtCore.QRect(10, 450, 101, 21))
        self.Evasion_label.setObjectName("Evasion_label")
        self.EvasionScaling_label = QtWidgets.QLabel(self.groupBox)
        self.EvasionScaling_label.setGeometry(QtCore.QRect(10, 480, 101, 21))
        self.EvasionScaling_label.setObjectName("EvasionScaling_label")
        self.Weight_label = QtWidgets.QLabel(self.groupBox)
        self.Weight_label.setGeometry(QtCore.QRect(10, 510, 101, 21))
        self.Weight_label.setObjectName("Weight_label")
        self.WeightScaling_label = QtWidgets.QLabel(self.groupBox)
        self.WeightScaling_label.setGeometry(QtCore.QRect(10, 540, 101, 21))
        self.WeightScaling_label.setObjectName("WeightScaling_label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(620, 660, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 10, 21, 691))
        self.line.setMaximumSize(QtCore.QSize(21, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveFileButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveFileButton_2.setGeometry(QtCore.QRect(218, 660, 193, 23))
        self.saveFileButton_2.setObjectName("saveFileButton_2")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(417, 660, 192, 23))
        self.exitButton.setObjectName("exitButton")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(20, 660, 192, 23))
        self.openFileButton.setObjectName("openFileButton")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 690, 1141, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1140, 10, 21, 691))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.fileName = QtWidgets.QLabel(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(20, 630, 261, 16))
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, -10, 1141, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.loadedCount = QtWidgets.QLCDNumber(self.centralwidget)
        self.loadedCount.setGeometry(QtCore.QRect(960, 640, 64, 23))
        self.loadedCount.setObjectName("loadedCount")
        self.listItems.raise_()
        self.groupBox.raise_()
        self.comboBox.raise_()
        self.line.raise_()
        self.saveFileButton_2.raise_()
        self.exitButton.raise_()
        self.openFileButton.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.fileName.raise_()
        self.HPBase_label.raise_()
        self.MinDMGScaling.raise_()
        self.MaxDMGScaling.raise_()
        self.MinDMGScaling_label.raise_()
        self.FeverSpeed.raise_()
        self.HPScaling_label.raise_()
        self.MinDMG_label.raise_()
        self.SprintSpeed_label.raise_()
        self.labelFeverSpeed_label.raise_()
        self.MaxDMG_label.raise_()
        self.HPScaling.raise_()
        self.MinDMG.raise_()
        self.MaxDMG.raise_()
        self.SprintSpeed.raise_()
        self.HPBase.raise_()
        self.MaxDMGScaling_label.raise_()
        self.line_3.raise_()
        self.loadedCount.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Potapon Resource File Editor"))
        self.HPBase_label.setText(_translate("MainWindow", "HP Base"))
        self.MinDMGScaling_label.setText(_translate("MainWindow", "Min DMG Scaling"))
        self.HPScaling_label.setText(_translate("MainWindow", "HP Scaling"))
        self.MinDMG_label.setText(_translate("MainWindow", "Min DMG"))
        self.SprintSpeed_label.setText(_translate("MainWindow", "Sprint Speed"))
        self.labelFeverSpeed_label.setText(_translate("MainWindow", "Fever Speed"))
        self.MaxDMG_label.setText(_translate("MainWindow", "MaxDMG"))
        self.MaxDMGScaling_label.setText(_translate("MainWindow", "Max DMG Scaling"))
        self.groupBox.setTitle(_translate("MainWindow", "BaseStats"))
        self.PowerScaling_label.setText(_translate("MainWindow", "Power Scaling"))
        self.ShieldBreak_label.setText(_translate("MainWindow", "Shield Break"))
        self.ShieldBreakScaling_label.setText(_translate("MainWindow", "Shield Break Scaling"))
        self.Power_label.setText(_translate("MainWindow", "Power"))
        self.Defense_label.setText(_translate("MainWindow", "Defense"))
        self.DefenseScaling_label.setText(_translate("MainWindow", "Defense Scaling"))
        self.Evasion_label.setText(_translate("MainWindow", "Evasion"))
        self.EvasionScaling_label.setText(_translate("MainWindow", "Evasion Scaling"))
        self.Weight_label.setText(_translate("MainWindow", "Weight"))
        self.WeightScaling_label.setText(_translate("MainWindow", "Weight Scaling"))
        self.saveFileButton_2.setText(_translate("MainWindow", "Сохранить файл"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.openFileButton.setText(_translate("MainWindow", " Открыть файл"))
