from abc import ABC, abstractmethod

class ILog(ABC):
    @abstractmethod
    def registrar(self, msg):
        pass

class LogArquivo(ILog):
    def registrar(self, msg):
        print(f"Registre'{msg}' no arquivo de log.")

class LogConsole(ILog):
    def registrar(self, msg):
        print(f"Registre '{msg}' na console.")

class LogBancoDeDados(ILog):
    def registrar(self, msg):
        print(f"Registre'{msg}' no banco de dados.")

class LogFactory:
    @staticmethod
    def criar_log(tipo):
        if tipo == 'arquivo':
            return LogArquivo()
        elif tipo == 'console':
            return LogConsole()
        elif tipo == 'banco_de_dados':
            return LogBancoDeDados()
        else:
            raise ValueError("Esse tipo de log é inválido")

factory = LogFactory

log = factory.criar_log('arquivo')
log.registrar('Log de arquivo criado com sucesso.')

log = factory.criar_log('console')
log.registrar('Log de console criado com sucesso.')

log = factory.criar_log('banco_de_dados')
log.registrar('Log de banco de dados criado com sucesso.')

print(factory.criar_log('arquivo'))  
print(factory.criar_log('console'))
print(factory.criar_log('banco_de_dados')) 