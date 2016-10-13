#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Miguel Suez Xve Penteado

Aqui eu defino uma janela dentro de da função principal.

1 - Inicio a aplicacao instanciando variável minha_aplicacao

2- "Desenho" a janela passando parametros para variável janela

3- Mostro a janela, chamando o método show() da variável janela.

4- Quando a janela termina, mato a aplicação dando exit 
na variável minha_aplicacao. 

"""



import sys
from PyQt4 import QtGui


def main():
    
    minha_aplicacao = QtGui.QApplication(sys.argv)

    janela = QtGui.QWidget()
    janela.resize(250, 150)
    janela.move(300, 300)
    janela.setWindowTitle('Janela Simples !')    
    janela.show()
    
    sys.exit(minha_aplicacao.exec_())


if __name__ == '__main__':
    main()

