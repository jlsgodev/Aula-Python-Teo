#Faça um programa que verifique se a pessoa pertence à família “calvo”.


nome = input ("Entre com seu nome completo: ")  # lê uma string

if "calvo" in nome.lower():                     # se "calvo" estiver em nome, (.lower converte a string para minúsculas)
    print("Você pertence à família Calvo")      # imprime a mensagem

else:                                           # senão
    print("Você não pertence à família Calvo")  # imprime a mensagem

