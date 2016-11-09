import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def aplicacao_principal():
   aplicacao = QApplication(sys.argv)
   janela_principal = QDialog()
   botao_1 = QPushButton(janela_principal)
   botao_1.setText("Botao 1")
   botao_1.move(50,20)

   botao_1.clicked.connect(funcao_botao_1)

   botao_2 = QPushButton(janela_principal)
   botao_2.setText("Botao 2")
   botao_2.move(50,50)

   QObject.connect(botao_2,SIGNAL("clicked()"),funcao_botao_2)

   janela_principal.setGeometry(100,100,200,100)
   janela_principal.setWindowTitle("QT com Python - PyQt")
   janela_principal.show()
   sys.exit(aplicacao.exec_())

def funcao_botao_1():
   print "Botao 1 apertado"

def funcao_botao_2():
   print "Botao 2 apertado"

if __name__ == '__main__':
   aplicacao_principal()
