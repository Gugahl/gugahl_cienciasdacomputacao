"""Exercício 08 - Caixa registradora"""
"""
Faça um programa que implemente uma caixa registradora rudimentar. O
programa deverá receber um número desconhecido de valores referentes
aos preços das mercadorias. Um valor zero deve ser informado pelo
operador para indicar o final da compra. O programa deve então mostrar o
total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa
deverá voltar ao ponto inicial, para registrar a próxima compra. Para o
programa encerrar por completo o usuário deve inserir o valor de -1. A saída
deve ser conforme o exemplo abaixo, o que está entre parênteses é apenas
explicativo e não deve ser printado:
Lojas Tabajara (Print inicial do nome da loja)
Produto 1: R$ 2.20 (Sequência de preços de produtos)
Produto 2: R$ 5.80
Produto 3: R$ 0 (Fim da compra)
Total: R$ 8.00 (Soma do total)
Dinheiro: R$ 20.00 (Valor de pagamento)
Troco: R$ 12.00 (Valor de troco)
Produto 1: R$ -1 (Início de uma nova compra, -1 para o programa)
Fim do programa.
"""

loja = 'Lojas Americanas'
print(f'=-' * 20 + f'\n' + f'{loja:^40}' + f'\n' + f'=-' * 20)

soma = troco = flag = cont = 0
while flag != -1:
    cont += 1
    preco = float(input(f'Digite o valor do {cont}º produto: R$'))
    if preco != 0:
        soma += preco
    if preco == flag:
        print(f'Total: R${soma:.2f}')
        pagamento = float(input('Digite qual o valor que você deseja dar para o pagamento: R$'))
        troco = pagamento - soma
        while troco < 0:
            adicional = float(input(f'Ainda falta R${-(troco):.2f} para concluirmos a compra: R$'))
            troco += adicional
        if troco >= 0:
            print(f'Seu troco foi: R${troco:.2f}\nObrigado pela preferência!')
            cont = 0
    if preco == -1:
        break
print('Fim do programa.')
