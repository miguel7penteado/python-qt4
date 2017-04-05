from progresso import Ui_Dialog
from PyQt4 import QtCore, QtGui
import sys, time

class FluxoAlternativo(QtCore.QThread):
    '''Public'''
    contador = None

    '''Construtor'''
    def __init__(self,parent,parametro_contagem):
        QtCore.QThread.__init__(self,parent) 
        self.contador = parametro_contagem

    '''Metodos'''
    def run(self):
        contador_local = 0
        self.emit(QtCore.SIGNAL("tamanho_total(PyQt_PyObject)"),self.contador)
        contador_local = 0
        while (contador_local < self.contador):
            if ( time.time()%1 == 0 ):
                contador_local += 1
                print str( contador_local )
                self.emit(QtCore.SIGNAL("atualizar()"))

# cria o dialogo
class Progresso(QtGui.QDialog):
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        # Configura uma interface de usuario a partir do Qt Designer. 
        self.interface_usuario  = Ui_Dialog()
        self.fluxo_alternativo  = FluxoAlternativo(self,100)

        self.interface_usuario.setupUi(self)
        self.interface_usuario.progressBar.setValue(0)

        QtCore.QObject.connect(self.fluxo_alternativo, QtCore.SIGNAL("tamanho_total(PyQt_PyObject)"), self.funcao_tamanho_total)
        QtCore.QObject.connect(self.fluxo_alternativo, QtCore.SIGNAL("atualizar()"), self.funcao_atualizar)

        self.contador = 0
        self.fluxo_alternativo.start()

    def funcao_atualizar(self):
        self.contador += 1
        print self.contador
        self.interface_usuario.progressBar.setValue(self.contador)

    def funcao_tamanho_total(self,parametro_total):
        self.interface_usuario.progressoBar.setMaximum(parametro_total)

if __name__=="__main__":
    aplicacao = QtGui.QApplication([])
    janela  = Progresso()
    janela.show()
    sys.exit(aplicacao.exec_())

    
