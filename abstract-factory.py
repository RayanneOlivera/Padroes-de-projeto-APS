from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def clique(self):
        pass

class WindowsBotao(Botao):
    def clique(self):
        return "Clicou no botão do Windows"

class MacOSBotao(Botao):
    def clique(self):
        return "Clicou no botão do MacOS"

class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self):
        pass

class WindowsFactory(GUIFactory):
    def criar_botao(self):
        return WindowsBotao()

class MacOSFactory(GUIFactory):
    def criar_botao(self):
        return MacOSBotao()

def cliente(factory: GUIFactory):
    botao = factory.criar_botao()
    print(botao.clique())


cliente(WindowsFactory())  
cliente(MacOSFactory())  

print(WindowsFactory().criar_botao())
print(MacOSFactory().criar_botao())
