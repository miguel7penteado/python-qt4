#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Miguel Suez Xve Penteado
"""

import sys
from PyQt4 import QtGui


class MeuExemplo(QtGui.QWidget):
    
    def __init__(self):
        super(MeuExemplo, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('Isto eh um componente <b>QWidget</b>')
        
        esse_botao = QtGui.QPushButton('Button', self)
        esse_botao.setToolTip('Isto eh um componente <b>QPushButton</b>')
        esse_botao.resize(esse_botao.sizeHint())
        esse_botao.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()
        
def main():
    
    aplicacao = QtGui.QApplication(sys.argv)
    ex = MeuExemplo()
    sys.exit(aplicacao.exec_())


if __name__ == '__main__':
    main()
