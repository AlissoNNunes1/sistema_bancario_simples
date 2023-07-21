menu = '''[1] Sacar
[2] Depositar
[3] Visualizar extrato
[0] Sair'''

saldo = 0
limite_diario = 3
saques_diarios = 0
movimentacoes = []  # Lista de movimentações (depósitos e saques)

while True:
    print(menu)
    opcao = int(input('Selecione a Opção: '))

    if opcao == 0:
        print('Saindo...')
        break
    elif opcao == 2:
        while True:
            valor_deposito = float(input('Quanto deseja depositar? '))
            if valor_deposito > 0:
                saldo += valor_deposito
                movimentacoes.append({'tipo': 'deposito', 'valor': valor_deposito})
                print(f'Depósito de R$ {valor_deposito:.2f} realizado. Novo saldo: R$ {saldo:.2f}')
                break
            else:
                print("O valor do depósito deve ser positivo. Tente novamente.")
    elif opcao == 1:
        while saques_diarios < limite_diario:
            valor_saque = float(input('Quanto deseja sacar? '))
            if valor_saque > saldo:
                print('Você não possui saldo suficiente.')
                break
            elif valor_saque > 500:
                print('Seu limite de saque diário é de R$ 500,00 reais.')
                break
            else:
                saldo -= valor_saque
                saques_diarios += 1
                movimentacoes.append({'tipo': 'saque', 'valor': valor_saque})
                print(f'Saque de R$ {valor_saque:.2f} realizado. Novo saldo: R$ {saldo:.2f}')
        else:
            print('Limite máximo de saques diários atingido.')
    elif opcao == 3:
        if not movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimentacao in movimentacoes:
                valor = movimentacao['valor']
                tipo = movimentacao['tipo']

                if tipo == 'deposito':
                    print(f"Depósito: R$ {valor:.2f}")
                elif tipo == 'saque':
                    print(f"Saque: R$ {valor:.2f}")

            print(f"Saldo atual da conta: R$ {saldo:.2f}")
    else:
        print('Opção inválida. Tente novamente.')
