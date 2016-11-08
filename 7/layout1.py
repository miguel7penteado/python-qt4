
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def janela():
   aplicacao = QApplication(sys.argv)
   minha_janela = QWidget()
	
   botao_1 = QPushButton("Botao 1")
   botao_2 = QPushButton("Botao 2")
   
   caixa_vertical = QVBoxLayout()
   caixa_vertical.addWidget(botao_1)
   caixa_vertical.addStretch()
   '''
   A funcao addStrech adiciona um espaco 
   esticavel entre botao_1
   e botao_2.   
   '''
   caixa_vertical.addWidget(botao_2)
   
   '''
   Caixa vertical eh associada ao layout
   da minha_janela. Entao, se minha_janela
   for redimensionada, entao os botoes
   associados a caixa_vertical serao
   reposicionados.
   '''
   minha_janela.setLayout(caixa_vertical)

   minha_janela.setWindowTitle("PyQt")
   minha_janela.show()
   sys.exit(aplicacao.exec_())

if __name__ == '__main__':
   janela()
