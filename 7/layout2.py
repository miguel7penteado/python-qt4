import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def janela():
   aplicacao = QApplication(sys.argv)
   janela = QWidget()

   botao_1 = QPushButton("Botao 1")
   botao_2 = QPushButton("Botao 2")
	
   caixa_vertical = QVBoxLayout()
   caixa_vertical.addWidget(botao_1)
   caixa_vertical.addStretch()
   caixa_vertical.addWidget(botao_2)
   
   caixa_horizontal = QHBoxLayout()
	
   botao_3 = QPushButton("Botao 3")
   botao_4 = QPushButton("Botao 4")
   caixa_horizontal.addWidget(botao_3)
   caixa_horizontal.addStretch()
   caixa_horizontal.addWidget(botao_4)

   caixa_vertical.addStretch()
   caixa_vertical.addLayout(caixa_horizontal)
   janela.setLayout(caixa_vertical)

   janela.setWindowTitle("Tested de Layout - PyQt")
   janela.show()
   sys.exit(aplicacao.exec_())

if __name__ == '__main__':
   janela()
   
