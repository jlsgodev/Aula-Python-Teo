# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Entre com seu nome completo: ")  # lê uma string

nome = nome.lower()  # converte a string para minúsculas

if "calvo" in nome or "silva" in nome:  # se "calvo" ou "silva" estiver em nome
    print("Você pertence à família Calvo ou Silva")  # imprime a mensagem

else:  # senão  
    print("Você não pertence à família Calvo ou Silva")

