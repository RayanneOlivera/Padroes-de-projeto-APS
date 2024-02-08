class Configuracao:
    __instance = None

    def __new__(cls, tema='claro', idioma='português', tamanho_fonte=12):
        if cls.__instance is None:
            cls.__instance = super(Configuracao, cls).__new__(cls)
            cls.__instance.tema = tema
            cls.__instance.idioma = idioma
            cls.__instance.tamanho_fonte = tamanho_fonte
        return cls.__instance


config = Configuracao()
print(config.tema) 
config.tema = 'escuro'
print(config.tema)  


config2 = Configuracao()
print(config2.tema) 