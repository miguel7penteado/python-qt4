COMPILADOR                  = pyuic4
PARAMETROS_COMPILACAO       = 
PARAMETROS_LINKAGEM         = 
CODIGO_FONTE                = cadastro.ui
#CABECALHOS                  = -I./
NOME_PROJETO                = cadastro.py


all: %.py
	echo ""
	@echo "************************************************************"
	@echo "Gerado o binário executável Exclusão Mútua... "
	@echo "************************************************************" 
	@echo ""
	
%.py: %.ui
	$(COMPILADOR) $(CODIGO_FONTE) -o $(NOME_PROJETO)


clean:
	@echo ""
	@echo "************************************************************************"
	@echo "Limpando arquivos da compilacao e linkagem do projeto Exclusão Mútua... "
	@echo "************************************************************************" 
	rm *.pyc

###### EDIT ##################### 
#Directory with ui and resource files
DIRETORIO_RECURSOS = ./recursos
 
#Directory for compiled etapa_recursos
DIRETORIO_COMPILADOS = ./compilados
 
#UI files to compile
ARQUIVOS_INTERFACE = confirm.ui main.ui repair.ui settings.ui statistics.ui
#Qt resource files to compile
ARQUIVOS_RECURSOS = 
 
#pyuic4 and pyrcc4 binaries
COMPILADOR_INTERFACES = pyuic4.bat
COMPILADOR_RECURSOS = pyrcc4
 
#################################
# DO NOT EDIT FOLLOWING
 
INTERFACES_COMPILADAS = $(ARQUIVOS_INTERFACE:%.ui=$(DIRETORIO_COMPILADOS)/ui_%.py)
RECURSOS_COMPILADOS = $(ARQUIVOS_RECURSOS:%.qrc=$(DIRETORIO_COMPILADOS)/%_rc.py)
 
all : etapa_recursos etapa_interfaces 
 
etapa_recursos : $(RECURSOS_COMPILADOS) 
 
etapa_interfaces : $(INTERFACES_COMPILADAS)
 
$(DIRETORIO_COMPILADOS)/ui_%.py : $(DIRETORIO_RECURSOS)/%.ui
	$(COMPILADOR_INTERFACES) $< -o $@
 
$(DIRETORIO_COMPILADOS)/%_rc.py : $(DIRETORIO_RECURSOS)/%.qrc
	$(COMPILADOR_RECURSOS) $< -o $@
 
clean : 
	$(RM) $(INTERFACES_COMPILADAS) $(RECURSOS_COMPILADOS) $(INTERFACES_COMPILADAS:.py=.pyc) $(RECURSOS_COMPILADOS:.py=.pyc)  
