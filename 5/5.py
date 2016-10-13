#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Miguel Suez Xve Penteado
"""

import sys
from PyQt4 import QtGui

"""=================================================================="""
"""    CLASSE QUE DESENHA A JANELA                                   """
"""=================================================================="""

""" Aqui eu defino um objeto janela atraves de uma classe"""
class MinhaClasse(QtGui.QWidget):

    """ Aqui estou chamando o construtor da classe pai"""    
    def __init__(self):
        super(MinhaClasse, self).__init__()
        
        self.initUI()
        
    """Desenhando a janela Principal"""    
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Caixa de Mensagem')    
        self.show()
        
    """Definindo o que executar no evento de fechamento da janela"""    
    def closeEvent(self, event):
        
        RespostaRecebida = QtGui.QMessageBox.question(self, 'Mensagem', "Voce te certeza que deseja sair ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if RespostaRecebida == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
"""=================================================================="""


"""=================================================================="""
"""                 Main                                             """
"""=================================================================="""
def main():
    
    minha_aplicacao = QtGui.QApplication(sys.argv)

    objeto_jabela_principal = MinhaClasse()

    sys.exit(minha_aplicacao.exec_())


if __name__ == '__main__':
    main()
    
