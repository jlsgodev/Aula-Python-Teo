#Faça um programa que receba uma quantidade indefinida de valores 
# correspondentes a “saldo em conta”, mas quando o usuário 
# apertar “enter” sem digitar valor algum, o programa para de 
# receber valores, e exibe a soma te todos 

total = 0  # inicializa a variável total

while True:
    entrada =input("Entre com o saldo em conta: ")  # lê uma string

    if entrada == "":  # se a entrada for vazia
        break
    total += float(entrada)  # converte a entrada para float e soma a total

print(f"A soma dos saldos em conta é {total}")  # imprime a mensagem

