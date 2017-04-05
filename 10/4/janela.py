# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(947, 558)
        self.progressoFluxo1 = QtGui.QProgressBar(Dialog)
        self.progressoFluxo1.setGeometry(QtCore.QRect(170, 70, 521, 23))
        self.progressoFluxo1.setProperty("value", 20)
        self.progressoFluxo1.setObjectName(_fromUtf8("progressoFluxo1"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 50, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressoFluxo2 = QtGui.QProgressBar(Dialog)
        self.progressoFluxo2.setGeometry(QtCore.QRect(170, 150, 521, 23))
        self.progressoFluxo2.setProperty("value", 20)
        self.progressoFluxo2.setObjectName(_fromUtf8("progressoFluxo2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Fluxo 1 - 1 s", None))
        self.label_2.setText(_translate("Dialog", "Fluxo 2 - 1 s", None))

