from Destino import Destino

class DestinoRepository:
    lista_destino: Destino = []

    def __init__(self):
        pass

    def adicioanar_destino(self, destino : Destino) -> None:
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd : int) -> bool:
        for destino in self.lista_destino:
            if(destino.DDD == ddd):
                return True

        return False


    def obter_destino_pelo_ddd(self, ddd : int) -> str:
        for destino in self.lista_destino:
            if(destino.DDD == ddd):
                return destino.destino
