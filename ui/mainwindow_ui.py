# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(520, 400)
        MainWindow.setMinimumSize(QtCore.QSize(520, 400))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setObjectName("label_1")
        self.horizontal_layout_1.addWidget(self.label_1)
        self.push_button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_1.sizePolicy().hasHeightForWidth())
        self.push_button_1.setSizePolicy(sizePolicy)
        self.push_button_1.setObjectName("push_button_1")
        self.horizontal_layout_1.addWidget(self.push_button_1)
        self.vertical_layout_1.addLayout(self.horizontal_layout_1)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontal_layout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem)
        self.check_box_1 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_box_1.sizePolicy().hasHeightForWidth())
        self.check_box_1.setSizePolicy(sizePolicy)
        self.check_box_1.setObjectName("check_box_1")
        self.horizontal_layout_2.addWidget(self.check_box_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem1)
        self.vertical_layout_1.addLayout(self.horizontal_layout_2)
        self.list_widget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_1.setObjectName("list_widget_1")
        self.vertical_layout_1.addWidget(self.list_widget_1)
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontal_layout_3.addWidget(self.label_3)
        self.push_button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_2.sizePolicy().hasHeightForWidth())
        self.push_button_2.setSizePolicy(sizePolicy)
        self.push_button_2.setObjectName("push_button_2")
        self.horizontal_layout_3.addWidget(self.push_button_2)
        self.vertical_layout_1.addLayout(self.horizontal_layout_3)
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontal_layout_4.addWidget(self.label_4)
        self.line_edit_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_1.sizePolicy().hasHeightForWidth())
        self.line_edit_1.setSizePolicy(sizePolicy)
        self.line_edit_1.setMinimumSize(QtCore.QSize(200, 0))
        self.line_edit_1.setObjectName("line_edit_1")
        self.horizontal_layout_4.addWidget(self.line_edit_1)
        self.vertical_layout_1.addLayout(self.horizontal_layout_4)
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        self.push_button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_3.sizePolicy().hasHeightForWidth())
        self.push_button_3.setSizePolicy(sizePolicy)
        self.push_button_3.setObjectName("push_button_3")
        self.horizontal_layout_5.addWidget(self.push_button_3)
        self.push_button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_4.sizePolicy().hasHeightForWidth())
        self.push_button_4.setSizePolicy(sizePolicy)
        self.push_button_4.setObjectName("push_button_4")
        self.horizontal_layout_5.addWidget(self.push_button_4)
        self.push_button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_5.sizePolicy().hasHeightForWidth())
        self.push_button_5.setSizePolicy(sizePolicy)
        self.push_button_5.setObjectName("push_button_5")
        self.horizontal_layout_5.addWidget(self.push_button_5)
        self.vertical_layout_1.addLayout(self.horizontal_layout_5)
        self.gridLayout.addLayout(self.vertical_layout_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 19))
        self.menubar.setObjectName("menubar")
        self.menuPomoc = QtWidgets.QMenu(self.menubar)
        self.menuPomoc.setObjectName("menuPomoc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUstawienia = QtWidgets.QAction(MainWindow)
        self.actionUstawienia.setObjectName("actionUstawienia")
        self.actionInstrukcja_uzycia = QtWidgets.QAction(MainWindow)
        self.actionInstrukcja_uzycia.setObjectName("actionInstrukcja_uzycia")
        self.actionO_GPandoc = QtWidgets.QAction(MainWindow)
        self.actionO_GPandoc.setObjectName("actionO_GPandoc")
        self.menuPomoc.addAction(self.actionUstawienia)
        self.menuPomoc.addAction(self.actionInstrukcja_uzycia)
        self.menuPomoc.addSeparator()
        self.menuPomoc.addAction(self.actionO_GPandoc)
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gPandoc"))
        self.label_1.setText(_translate("MainWindow", "1. Zaimportuj pliki: "))
        self.push_button_1.setText(_translate("MainWindow", "Wybierz pliki"))
        self.label_2.setText(_translate("MainWindow", "Lista wybranych plików: "))
        self.check_box_1.setText(_translate("MainWindow", "Łącz dokumenty"))
        self.label_3.setText(_translate("MainWindow", "2. Przepis (Wygląd i rozszerzenie): "))
        self.push_button_2.setText(_translate("MainWindow", "Wybierz przepis"))
        self.label_4.setText(_translate("MainWindow", "3. Nazwa dokumentu(bez rozszerzenia): "))
        self.push_button_3.setText(_translate("MainWindow", "Wygeneruj"))
        self.push_button_4.setText(_translate("MainWindow", "Usuń zaznaczone"))
        self.push_button_5.setText(_translate("MainWindow", "Usuń wszystko"))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc"))
        self.actionUstawienia.setText(_translate("MainWindow", "Ustawienia"))
        self.actionInstrukcja_uzycia.setText(_translate("MainWindow", "Instrukcja użycia"))
        self.actionO_GPandoc.setText(_translate("MainWindow", "O gPandoc"))

