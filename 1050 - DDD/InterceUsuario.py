from DestinoRepository import DestinoRepository

class InterfaceUsuario:

    def __init__(self, destino_repository : DestinoRepository) -> None:
        self.destino_repository = destino_repository

    def solicitar_input_usuario(self):
        result = int(input("Por favor informe o um DDD: "))
        return result

    def exibir_destinos(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "Destino")

        for destino in self.destino_repository.lista_destino:
            menu += formatText.format(destino.DDD, destino.destino)

        return menu

    def saida_usuario(self):
        ddd = self.solicitar_input_usuario()

        if (not self.destino_repository.checa_se_destino_existe(ddd)):
            print("DDD nao cadastrado")
            return False

        print(f"Destino: {self.destino_repository.obter_destino_pelo_ddd(ddd)}")
        return True