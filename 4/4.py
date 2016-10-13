#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Miguel Suez Xve Penteado

"""

import sys
from PyQt4 import QtGui, QtCore


class MinhaClasse(QtGui.QWidget):
    
    def __init__(self):
        super(MinhaClasse, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        botao_ordinario = QtGui.QPushButton('Sair', self)
        
        botao_ordinario.clicked.connect(QtCore.QCoreApplication.instance().quit)
        botao_ordinario.resize(botao_ordinario.sizeHint())
        botao_ordinario.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Botao Sair')    
        self.show()
        
def main():
    
    aplicacao = QtGui.QApplication(sys.argv)
    ex = MinhaClasse()
    sys.exit(aplicacao.exec_())


if __name__ == '__main__':
    main()
