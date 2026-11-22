from caixa import adicionar_item, calcular_total, remover_item, trocar_item, aplicar_desconto, salvar_pedido, carregar_pedido
import os

cardapio = {"xis": 25, "batata-frita": 15, "refri": 8, "suco": 8}


def test_adicionar_varios_itens():
    pedido = []
    adicionar_item(pedido, cardapio, "xis", "refri", "batata-frita")
    assert pedido == ["xis", "refri", "batata-frita"]

def test_total_pedido_vazio():
    pedido = []
    assert calcular_total(pedido, cardapio) == 0

def test_remover_item():
    pedido = ["xis", "refri"]
    remover_item(pedido, "xis")
    assert pedido == ["refri"]

def test_adicionar_item_inexistente():
    pedido = ["xis"]
    adicionar_item(pedido, cardapio, "pizza")
    assert pedido == ["xis"]

def test_desconto_padrao():
    pedido = ["xis", "refri"]
    assert aplicar_desconto(100) == 90

def test_trocar_item():
    pedido = ["xis", "refri", "batata-frita"]
    trocar_item(pedido, cardapio, "xis", "suco")
    assert pedido == ["suco", "refri", "batata-frita"]

def test_salvar_e_carregar(tmp_path):
    caminho = tmp_path / "pedido.json"
    pedido = ["xis", "refri"]

    salvar_pedido(pedido, caminho)              # lacuna 1
    pedido_carregado = carregar_pedido(caminho) # lacuna 2

    assert pedido_carregado == pedido                      # lacuna 3

def test_carregar_arquivo_inexistente(tmp_path):
    caminho = tmp_path / "pedido.json"       # o caminho existe, mas o arquivo NÃO
    pedido_carregado = carregar_pedido(caminho) # lacuna 1

    assert pedido_carregado == []          # lacuna 2

def test_carregar_arquivo_corrompido(tmp_path):
    caminho = tmp_path / "pedido.json"
    with open(caminho, "w") as arquivo:
        arquivo.write("{abc")

    pedido_carregado = carregar_pedido(caminho)

    assert pedido_carregado == []
    assert os.path.exists(f"{caminho}.bak")
    assert not os.path.exists(caminho)