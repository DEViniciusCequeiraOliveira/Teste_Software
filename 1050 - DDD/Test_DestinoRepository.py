from DestinoRepository import DestinoRepository
from Destino import Destino

def test_adiciona_destino():
    # Arrange
    destino_repository = DestinoRepository();
    destino_repository.lista_destino = []
    destino1 = Destino(75, "Feira de Santana")
    destino2 = Destino(85, "Fortal")
    destino3 = Destino(00, "Teste")

    # Act
    destino_repository.adicioanar_destino(destino1)
    destino_repository.adicioanar_destino(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 2
    assert not destino3 in destino_repository.lista_destino
    assert type(destino_repository.lista_destino) == list

def test_check_if_destino_exists():
    # Arrange
    destino_repository = DestinoRepository();
    destino_repository.lista_destino = []
    destino1 = Destino(1, "Destino01")
    destino2 = Destino(2, "Destino02")
    destino_repository.adicioanar_destino(destino1)

    # Act
    resultOK = destino_repository.checa_se_destino_existe(1)
    resultNOK = destino_repository.checa_se_destino_existe(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 1
    assert resultOK == True
    assert resultNOK == False

def test_obter_destino_pelo_ddd():
    # Arrange
    destino_repository = DestinoRepository();
    destino_repository.lista_destino = []
    destino_repository.adicioanar_destino(Destino(1, "Destino01"))

    # Act
    destinoOK = destino_repository.obter_destino_pelo_ddd(1)
    destinoNOK = destino_repository.obter_destino_pelo_ddd(2)

    # Assert
    assert destinoOK == "Destino01"
    assert destinoNOK is None

