#!/usr/bin/python

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

import modulo_cadastro.cadastro

class Aplicacao(QtGui.QMainWindow, modulo_cadastro.cadastro.Ui_JanelaPrincipal):
    # construtor
    def __init__(self, parent=None):
        super(Aplicacao, self).__init__(parent)
        self.setupUi(self)
	def dialogoAjuda(self):
		QMessageBox.about(self,"Sobre","Isto eh uma caixa de ajuda \n Mostrada via menu.")


def executar_inicio():
    aplicacao = QtGui.QApplication(sys.argv)
    formulario_principal = Aplicacao()
    #formulario_principal.AcaoSobre.Connection(dialogoAjuda)
    #QtCore.QObject.connect(formulario_principal.AcaoSobre, SIGNAL(triggered()), formulario_principal, SLOT(dialogoAjuda()));
    QtCore.QObject.connect(formulario_principal.AcaoSobre, QtCore.SIGNAL("triggered()"), formulario_principal.dialogoAjuda());
    formulario_principal.show()
    
#    QObject.connect(action,SIGNAL("triggered()"),formulario_principal,SLOT("dialogoAjuda()"))
    
    aplicacao.exec_()

if __name__ == '__main__':
    executar_inicio()



