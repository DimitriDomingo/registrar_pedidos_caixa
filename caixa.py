import json
import os

def adicionar_item(pedido, cardapio, *lanches):
    for lanche in lanches:
        if lanche not in cardapio:
            print("Item não existe no cardápio")
        else:
            pedido.append(lanche)


def calcular_total(pedido, cardapio):

    total = 0

    for item in pedido:
        total += cardapio[item]

    return total


def remover_item(pedido, item_remover):
    if item_remover in pedido:
        posicao = pedido.index(item_remover)
        pedido.pop(posicao)
    else:
        print(f"item {item_remover} não está no pedido")


def trocar_item(pedido, cardapio, item_trocar, item_novo):
    if item_trocar in pedido and item_novo in cardapio:
        posicao = pedido.index(item_trocar)
        pedido[posicao] = item_novo
    elif item_trocar not in pedido:
        print(f"item {item_trocar} não está no pedido")
    else:
        print(f"Item {item_novo} não está no cardápio")


def aplicar_desconto(total, percentual=10):
    porcentagem = percentual / 100
    desconto = total * porcentagem
    desconto = total - desconto

    return desconto

def salvar_pedido(pedido, nome_arquivo="pedido.json"):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(pedido, arquivo)

def carregar_pedido(nome_arquivo="pedido.json"):
    try:
        with open(nome_arquivo, "r") as arquivo:
            pedido_lido = json.load(arquivo)
            return pedido_lido
    except FileNotFoundError:
        print("O pedido está vazio")
        return []
    except json.JSONDecodeError:
        os.replace(nome_arquivo, f"{nome_arquivo}.bak")
        print("O arquivo está com problemas, criamos um backup")
        return []

cardapio = {"xis": 25, "batata-frita": 15, "refri": 8, "suco": 8}
pedido = []

if __name__ == "__main__":
    pedido = carregar_pedido()
    while True:
        print("=== Zemi Lanches ===")
        print ("1 - Ver cardápio")
        print ("2 - Adicionar item")
        print ("3 - Remover item")
        print ("4 - Ver pedido e total")
        print ("0 - Sair")


        decisao = (input("Digite a opção desejada: "))

        if decisao == "1":
            print (f"Cardápio da casa:\n {cardapio}")

        elif decisao == "2":
            lanche = str(input("Digite o item que deseja adicionar: "))
            adicionar_item(pedido, cardapio, lanche)

        elif decisao == "3":
            item_remover = str(input("O que desejja excluír: "))
            remover_item(pedido, item_remover)

        elif decisao == "4":
            total = calcular_total(pedido, cardapio)
            print(f"Seu pedido: {pedido}")
            print(f"Total: {total}")

        elif decisao == "0":
            salvar_pedido(pedido)
            break
        else:
            print("Opção inválida!")