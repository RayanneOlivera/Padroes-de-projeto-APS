from abc import ABC, abstractmethod

class OpenGL(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class OpenGLSingleton(OpenGL):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def renderizar(self):
        print("Renderizando com OpenGL")

class DirectX(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class DirectXSingleton(DirectX):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def renderizar(self):
        print("Renderizando com DirectX")

class RenderizadorFactory:
    def get_renderizador(self, tipo):
        if tipo == "opengl":
            return OpenGLSingleton()
        elif tipo == "directx":
            return DirectXSingleton()
        else:
            raise ValueError("Tipo de renderização é inválido")

factory = RenderizadorFactory()
opengl = factory.get_renderizador("opengl")
opengl.renderizar()
directx = factory.get_renderizador("directx")
directx.renderizar()
print(factory.get_renderizador("opengl"))
print(factory.get_renderizador("directx"))
