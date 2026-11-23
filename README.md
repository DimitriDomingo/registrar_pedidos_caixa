# Sistema registrador de pedidos

## O que é o sistema

Este sistema funciona como um caixa de lanchonete que roda no terminal, o diferencial dele é que o pedido fica salvo entre uma execução e outra em JSON.

## Funcionalidades

- Adicionar item
- Calcular total do pedido
- Remover item
- Salvar pedido
- Carregar pedido em JSON
- Trocar item do cardápio por outro **(funcionalidade existe mas ainda não está no MENU)**
- Aplicar desconto **(funcionalidade existe mas ainda não está no MENU)**

## Tecnologias

- Python
- JSON
- pytest

## Como rodar

**Pré-requisitos:** Python 3 e o pytest (para os testes)

```
pip install pytest
```

Clone o repositório e rode o programa:

```
git clone https://github.com/DimitriDomingo/registrar_pedidos_caixa.git

cd registrar_pedidos_caixa

python caixa.py
```

## Como rodar os testes

Para rodar os testes, você precisará utilizar o comando:

```
python -m pytest
```

Use diretamente no seu terminal, assim, ele fará todos os testes automaticamente.

## O que aprendi

- CRUD simples
- Tratamento de erros
- Refatoração de código
- Persistência de dados
- Testes isolados e automatizados