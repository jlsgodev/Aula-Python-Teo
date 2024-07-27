

# boolean , algoritmo para saber se pessoa tem idade e se  esta habilitado a dirigir
print("Qual a sua idade ?")
idade = int(input())
print("Você tem carteira de motorista ?")
carteira = input()
if idade >= 18 and carteira == "sim":  # se a idade for maior ou igual a 18 e a carteira for igual a sim
    print("Você está habilitado a dirigir") 
else:
    print("Você não está habilitado a dirigir")
    print("Preso em nome da Lei!")

