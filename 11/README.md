# Gerência de Memória

Uma aplicação pode potencialmente consumir muita memória
se, for example, não for tomado cuidados com o fechamento de componentes.
As classe baseadas em `QObject` são designadas para ser (opcionalmente) ligadas em hierarquia.
Quando um objeto no nivel do topo é `apagado`, Qt vai apagar automaticamente todos os objetos filhos.
Entretanto, quando se está `fechando` componentes (sendo estes subclasses de QObject), 
a deleção automatica apenas irá acontecer se o atributo `Qt.WA_DeleteOnClose `
estiver setado (e ele não é setado por padrão).
