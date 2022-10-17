from Destino import Destino
from DestinoRepository import DestinoRepository
from InterceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()

destino_repository.adicioanar_destino(Destino(61, "Brasilia"))
destino_repository.adicioanar_destino(Destino(71, "Salvador"))
destino_repository.adicioanar_destino(Destino(11, "São Paulo"))
destino_repository.adicioanar_destino(Destino(21, "Rio de Janeiro"))
destino_repository.adicioanar_destino(Destino(32, "Juiz de Fora"))
destino_repository.adicioanar_destino(Destino(19, "Campinas"))
destino_repository.adicioanar_destino(Destino(27, "Vitoria"))
destino_repository.adicioanar_destino(Destino(31, "Belo Horizonte"))

interface_usuario = InterfaceUsuario(destino_repository)

print(interface_usuario.exibir_destinos())

while interface_usuario.saida_usuario():
    pass