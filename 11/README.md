# Gerência de Memória

Uma aplicação pode potencialmente consumir muita memória
se, for example, não for tomado cuidados com o fechamento de componentes.
As classe baseadas em `QObject` são designadas para ser (opcionalmente) ligadas em hierarquia.
Quando um objeto no nivel do topo é `apagado`, Qt vai apagar automaticamente todos os objetos filhos.
Entretanto, quando se está `fechando` componentes (sendo estes subclasses de QObject), 
a deleção automatica apenas irá acontecer se o atributo `Qt.WA_DeleteOnClose `
estiver setado (e ele não é setado por padrão).

Com PyQt/PySide, existem 2 aspectos de posse de objetos : a **parte Python** e a **parte Qt** . Frequentemente, removendo a última referência Python a um objeto no é o suficiente para limpa-lo completamente, porque ainda pode haver uma referência para manter-lo no lado **Qt**.

Em geral, **Qt** tende a não implicitamente deletar objetos. Então se sua aplicação cria e remove vários **QObjects** (ou abre e fecha muitos componentes), você pode precisar tomar alguns passos para deletar-los explicitamente por questões de uso da memória.
