#!/usr/bin/python
# -*- coding: utf-8 -*-


"""

Miguel Suez Xve

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
        
        self.resize(250, 150)
        self.center()
        
        self.setWindowTitle('Centralizar')    
        self.show()
    
    """Centralizando a Janela Principal"""    
    def center(self):
        
        retangulo_janela = self.frameGeometry()
        resolucao_tela = QtGui.QDesktopWidget().availableGeometry().center()
        retangulo_janela.moveCenter(resolucao_tela)
        self.move(retangulo_janela.topLeft())
        
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
