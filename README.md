# Sistema Bancário simples

## Descrição
Desafio de Projeto da DIO Este é um programa simples de controle financeiro desenvolvido em Python. Ele permite ao usuário realizar operações de saque, depósito e visualização de extrato. O programa possui um limite diário de 3 saques, cada um limitado a R$ 500,00.

## Como usar
1. Execute o programa e siga as instruções apresentadas no menu.
2. Selecione a opção desejada digitando o número correspondente.
3. Para saques e depósitos, informe o valor desejado quando solicitado.
4. O programa exibirá mensagens de sucesso ou de erro, dependendo da operação realizada.
5. Para visualizar o extrato, selecione a opção correspondente. Caso ainda não tenha sido realizada nenhuma movimentação, o programa informará que não foram realizadas movimentações. Caso contrário, será exibida a lista de depósitos e saques realizados, seguida do saldo atual da conta.

## Menu de Opções
O menu de opções é exibido ao iniciar o programa e possui as seguintes funcionalidades:

[1] Sacar
[2] Depositar
[3] Visualizar extrato
[0] Sair

## Observações
- O valor do depósito deve ser positivo. Caso seja inserido um valor negativo, o programa solicitará que o usuário tente novamente.
- Caso o valor do saque seja maior que o saldo disponível na conta, o programa informará que não é possível realizar o saque.
- O programa possui um limite diário de 3 saques, cada um limitado a R$ 500,00. Ao atingir esse limite, o usuário não poderá fazer mais saques no mesmo dia.
- Caso o usuário selecione a opção de sair (0), o programa encerrará a execução.



