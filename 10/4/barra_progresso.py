#! /usr/bin/python


from janela import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, QThread, Qt
import sys, time


class BarraProgressosFluxo1(QObject):
    '''Atributos Public'''
    tamanho_contagem_fluxo1 = 100
    
    '''Construtor'''
    def __init__(self,parametro_contador=None):
        super(BarraProgressosFluxo1,self).__init__() 
        self.tamanho_contagem_fluxo1 = parametro_contador

    
    '''Metodos da Classe - sobrecarga do metodo run '''
    @QtCore.pyqtSlot()
    def executar(self):
        contador_laco = None
        self.emit(QtCore.SIGNAL("sinal_valor_maximo_fluxo1(PyQt_PyObject)"),self.tamanho_contagem_fluxo1)
        contador_laco=0
        while ( contador_laco < self.tamanho_contagem_fluxo1):
            if (time.time() % 1==0):
                contador_laco+=1
                print '\nFuncao run Fluxo 1 %s ' % str(contador_laco)
                self.emit(QtCore.SIGNAL("sinal_atualizar_fluxo1(PyQt_PyObject)"),contador_laco)


class BarraProgressosFluxo2(QObject):
    '''Atributos Public'''
    tamanho_contagem_fluxo2 = 100
    
    '''Construtor'''
    def __init__(self,parametro_contador=None):
        super(BarraProgressosFluxo2,self).__init__() 
        self.tamanho_contagem_fluxo2 = parametro_contador
    
    '''Metodos da Classe - sobrecarga do metodo run '''
    @QtCore.pyqtSlot()
    def executar(self):
        contador_laco = None
        
        self.emit(QtCore.SIGNAL("sinal_valor_maximo_fluxo2(PyQt_PyObject)"),self.tamanho_contagem_fluxo2)
        contador_laco=0
        while ( contador_laco < self.tamanho_contagem_fluxo2):
            if (time.time() % 1==0):
                contador_laco+=1
                print '\nFuncao run Fluxo 2 %s ' % str(contador_laco)
                self.emit(QtCore.SIGNAL("sinal_atualizar_fluxo2(PyQt_PyObject)"),contador_laco)


# create the dialog for zoom to point
class JanelaProgresso(QtGui.QDialog):
    '''Atributos Privados'''
    __fluxo_principal__              = None
    ___fluxo1___                     = None
    ___fluxo2___                     = None
    
    '''Atributos Public'''
    janela                           = None
    codigo_fluxo1                    = None
    #codigo_fluxo2                    = None
    
    contador_fluxo_principal         = None
    contador_fluxo_alternativo       = None
    
    tamanho_contagem_fluxo_principal = None
    
    '''Construtor'''
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        self.tamanho_contagem_fluxo_principal = 100
        self.contador_fluxo1                  = 0
        self.contador_fluxo2                  = 0
        
        self.janela = Ui_Dialog()
        self.janela.setupUi(self)
        
        self.janela.progressoFluxo1.setValue(0)
        self.janela.progressoFluxo2.setValue(0)
        
        self.__fluxo1__ = QThread()
        self.__fluxo2__ = QThread()        
        
        self.codigo_fluxo1 = BarraProgressosFluxo1(100)
        self.codigo_fluxo2 = BarraProgressosFluxo2(100)
        
        self.codigo_fluxo1.moveToThread(self.__fluxo1__)
        self.codigo_fluxo2.moveToThread(self.__fluxo2__)
        
        '''
        Qt.AutoConnection   -
        Qt.QueuedConnection -
        '''
        
        QtCore.QObject.connect(self, QtCore.SIGNAL("sinal_ativar_fluxo1()"), self.codigo_fluxo1 ,QtCore.SLOT('executar()'), Qt.QueuedConnection)
        QtCore.QObject.connect(self, QtCore.SIGNAL("sinal_ativar_fluxo2()"), self.codigo_fluxo2 ,QtCore.SLOT('executar()'), Qt.QueuedConnection)
        
        QtCore.QObject.connect(self.codigo_fluxo1, QtCore.SIGNAL("sinal_valor_maximo_fluxo1(PyQt_PyObject)"), self.definir_tamanho_total_fluxo1)
        QtCore.QObject.connect(self.codigo_fluxo2, QtCore.SIGNAL("sinal_valor_maximo_fluxo2(PyQt_PyObject)"), self.definir_tamanho_total_fluxo2)

        QtCore.QObject.connect(self.codigo_fluxo1, QtCore.SIGNAL("sinal_atualizar_fluxo1(PyQt_PyObject)"), self.atualizar_mostrador_fluxo1)
        QtCore.QObject.connect(self.codigo_fluxo2, QtCore.SIGNAL("sinal_atualizar_fluxo2(PyQt_PyObject)"), self.atualizar_mostrador_fluxo2)
        
        self.contador_barra=0

        self.__fluxo1__.start()
        self.__fluxo2__.start()
        self.fluxo_principal()



    '''Metodos da Classe '''
    def fluxo_principal(self):
        contador_laco = None
        
        self.emit(QtCore.SIGNAL("sinal_ativar_fluxo1()"))
        self.emit(QtCore.SIGNAL("sinal_ativar_fluxo2()"))
        
        
    
    def atualizar_mostrador_fluxo1(self,parametro_contado):
        self.contador_fluxo1 = parametro_contado
        print '\nsinal fluxo 1 %d' % self.contador_fluxo1
        self.janela.progressoFluxo1.setValue(self.contador_fluxo1)
    
    def atualizar_mostrador_fluxo2(self,parametro_contado):
        self.contador_fluxo2 = parametro_contado
        print '\nsinal fluxo 2 %d' % self.contador_fluxo2
        self.janela.progressoFluxo2.setValue(self.contador_fluxo2)

    def definir_tamanho_total_fluxo1(self,parametro_valor_maximo):
        self.tamanho_contagem_fluxo1 = parametro_valor_maximo
        print('\nsinal define valor maximo fluxo 1 %s') % parametro_valor_maximo
        self.janela.progressoFluxo1.setMaximum(parametro_valor_maximo)

    def definir_tamanho_total_fluxo2(self,parametro_valor_maximo):
        print('\nsinal define valor maximo fluxo 2 %s') % parametro_valor_maximo
        self.janela.progressoFluxo2.setMaximum(parametro_valor_maximo)


if __name__=="__main__":
    aplicacao = QtGui.QApplication([])
    janela = JanelaProgresso()
    janela.show()
    sys.exit(aplicacao.exec_())
