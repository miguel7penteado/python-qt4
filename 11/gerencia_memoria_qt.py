#! /usr/bin/python


from PyQt4 import QtCore, QtGui

class JanelaPai(QtGui.QWidget):
    '''
    public
    '''
    caixa_checagem = None
    botao          = None
    enquadramento  = None
        
    '''
    Construtor
    '''
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.caixa_checagem = QtGui.QCheckBox('Deletar')
        self.botao = QtGui.QPushButton('Abrir', self)
        self.botao.clicked.connect(self.openDialog)
        self.enquadramento = QtGui.QHBoxLayout(self)
        self.enquadramento.addWidget(self.caixa_checagem)
        self.enquadramento.addWidget(self.botao)

    def openDialog(self):
        janela_filha                  = QtGui.QDialog(self)
        rotulo_filho                = None
        botao_filho                 = None
        contador_objetos_em_memoria = None
        
        if (self.caixa_checagem.isChecked() and not janela_filha.testAttribute(QtCore.Qt.WA_DeleteOnClose)):
            
            janela_filha.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            
            for contador_objetos_em_memoria in self.findChildren(QtGui.QDialog):
                if contador_objetos_em_memoria is not janela_filha:
                    contador_objetos_em_memoria.deleteLater()
        
        rotulo_filho = QtGui.QLabel(janela_filha)
        botao_filho  = QtGui.QPushButton('Fechar', janela_filha)
        
        botao_filho.clicked.connect(janela_filha.close)
        
        self.enquadramento = QtGui.QVBoxLayout(janela_filha)
        self.enquadramento.addWidget(rotulo_filho)
        self.enquadramento.addWidget(botao_filho)

        vetor_objetos_filhos = self.findChildren(QtCore.QObject)
        rotulo_filho.setText('Objetos alocados = %d' % len(vetor_objetos_filhos))
        print(vetor_objetos_filhos)
        janela_filha.show()

if __name__ == '__main__':

    import sys
    aplicacao = QtGui.QApplication(sys.argv)
    janela_pai = JanelaPai()
    janela_pai.setGeometry(500, 300, 100, 50)
    janela_pai.show()
    sys.exit(aplicacao.exec_())
