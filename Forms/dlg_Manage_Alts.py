# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rammc\Documents\Pycharm3\BDO_Enhancement_Tool\Forms\dlg_Manage_Alts.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_Manage_Alts(object):
    def setupUi(self, dlg_Manage_Alts):
        dlg_Manage_Alts.setObjectName("dlg_Manage_Alts")
        dlg_Manage_Alts.resize(723, 501)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlg_Manage_Alts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(dlg_Manage_Alts)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 703, 434))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutAlts = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.layoutAlts.setObjectName("layoutAlts")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widget = QtWidgets.QWidget(dlg_Manage_Alts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmdAdd = QtWidgets.QPushButton(self.widget)
        self.cmdAdd.setAutoDefault(False)
        self.cmdAdd.setObjectName("cmdAdd")
        self.horizontalLayout.addWidget(self.cmdAdd)
        self.cmdImport = QtWidgets.QPushButton(self.widget)
        self.cmdImport.setAutoDefault(False)
        self.cmdImport.setObjectName("cmdImport")
        self.horizontalLayout.addWidget(self.cmdImport)
        spacerItem = QtWidgets.QSpacerItem(314, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOk = QtWidgets.QPushButton(self.widget)
        self.cmdOk.setAutoDefault(False)
        self.cmdOk.setObjectName("cmdOk")
        self.horizontalLayout.addWidget(self.cmdOk)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(dlg_Manage_Alts)
        QtCore.QMetaObject.connectSlotsByName(dlg_Manage_Alts)

    def retranslateUi(self, dlg_Manage_Alts):
        _translate = QtCore.QCoreApplication.translate
        dlg_Manage_Alts.setWindowTitle(_translate("dlg_Manage_Alts", "Manage Alts"))
        self.cmdAdd.setText(_translate("dlg_Manage_Alts", "Add Alt"))
        self.cmdImport.setText(_translate("dlg_Manage_Alts", "Import From Game Files"))
        self.cmdOk.setText(_translate("dlg_Manage_Alts", "OK"))

