#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Miguel Suez Xve Penteado

Aqui eu sigo a mesma idéia anterior

1 - Inicio a aplicacao 

2- "Desenho" a janela 

3- Mostro a janela, 

4- Mato a aplicação 

Só que agora os passos 2 e 3 foram separados da função
principal para deixar o código mais organizado.

A classe Exemplo desenha e mostra a aplicação.

A função principal quando inicializa a variável
Janela_Principal através da classe DesenhadorDeJanelas,
já recebe a janela formatada e mostrada na tela, no ato da
inicialização.

"""

import sys
from PyQt4 import QtGui

"""=================================================================="""
"""    CLASSE QUE DESENHA A JANELA                                   """
"""=================================================================="""
class DesenhadorDeJanelas(QtGui.QWidget):
    
    def __init__(self):
        super(DesenhadorDeJanelas, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icone')
        self.setWindowIcon(QtGui.QIcon('icon.png'))        
    
        self.show()        
"""=================================================================="""


"""=================================================================="""
"""                 Main                                             """
"""=================================================================="""
def main():
    
    aplicacao = QtGui.QApplication(sys.argv)
    
    Janela_Principal = DesenhadorDeJanelas()
    
    sys.exit(aplicacao.exec_())


if __name__ == '__main__':
    main()    
