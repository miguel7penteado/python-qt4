# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
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

class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName(_fromUtf8("JanelaPrincipal"))
        JanelaPrincipal.resize(945, 763)
        self.componente_central = QtGui.QWidget(JanelaPrincipal)
        self.componente_central.setObjectName(_fromUtf8("componente_central"))
        self.formLayoutWidget = QtGui.QWidget(self.componente_central)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 951, 721))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.layout_formulario = QtGui.QFormLayout(self.formLayoutWidget)
        self.layout_formulario.setObjectName(_fromUtf8("layout_formulario"))
        JanelaPrincipal.setCentralWidget(self.componente_central)
        self.menu_principal = QtGui.QMenuBar(JanelaPrincipal)
        self.menu_principal.setGeometry(QtCore.QRect(0, 0, 945, 19))
        self.menu_principal.setObjectName(_fromUtf8("menu_principal"))
        self.menuCadastrar = QtGui.QMenu(self.menu_principal)
        self.menuCadastrar.setObjectName(_fromUtf8("menuCadastrar"))
        self.menuSobre = QtGui.QMenu(self.menu_principal)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        JanelaPrincipal.setMenuBar(self.menu_principal)
        self.barra_status = QtGui.QStatusBar(JanelaPrincipal)
        self.barra_status.setObjectName(_fromUtf8("barra_status"))
        JanelaPrincipal.setStatusBar(self.barra_status)
        self.AcaoInserir = QtGui.QAction(JanelaPrincipal)
        self.AcaoInserir.setObjectName(_fromUtf8("AcaoInserir"))
        self.AcaoAlterar = QtGui.QAction(JanelaPrincipal)
        self.AcaoAlterar.setObjectName(_fromUtf8("AcaoAlterar"))
        self.AcaoRemover = QtGui.QAction(JanelaPrincipal)
        self.AcaoRemover.setObjectName(_fromUtf8("AcaoRemover"))
        self.AcaoPesquisar = QtGui.QAction(JanelaPrincipal)
        self.AcaoPesquisar.setObjectName(_fromUtf8("AcaoPesquisar"))
        self.AcaoSair = QtGui.QAction(JanelaPrincipal)
        self.AcaoSair.setObjectName(_fromUtf8("AcaoSair"))
        self.AcaoSobre = QtGui.QAction(JanelaPrincipal)
        self.AcaoSobre.setObjectName(_fromUtf8("AcaoSobre"))
        self.menuCadastrar.addAction(self.AcaoInserir)
        self.menuCadastrar.addAction(self.AcaoAlterar)
        self.menuCadastrar.addAction(self.AcaoRemover)
        self.menuCadastrar.addAction(self.AcaoPesquisar)
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.AcaoSair)
        self.menuSobre.addAction(self.AcaoSobre)
        self.menu_principal.addAction(self.menuCadastrar.menuAction())
        self.menu_principal.addAction(self.menuSobre.menuAction())

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "MainWindow", None))
        self.menuCadastrar.setTitle(_translate("JanelaPrincipal", "Cadastrar", None))
        self.menuSobre.setTitle(_translate("JanelaPrincipal", "Ajuda", None))
        self.AcaoInserir.setText(_translate("JanelaPrincipal", "Inserir", None))
        self.AcaoAlterar.setText(_translate("JanelaPrincipal", "Alterar", None))
        self.AcaoRemover.setText(_translate("JanelaPrincipal", "Remover", None))
        self.AcaoPesquisar.setText(_translate("JanelaPrincipal", "Pesquisar", None))
        self.AcaoSair.setText(_translate("JanelaPrincipal", "Sair", None))
        self.AcaoSobre.setText(_translate("JanelaPrincipal", "Sobre", None))

