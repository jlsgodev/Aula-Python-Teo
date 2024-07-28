#Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na 
# lista: laranja, cerveja, miojo, carvão, picanha.
# desta vez usando lista 
# %%
lista = ["laranja", "cerveja", "miojo", "carvão", "picanha"]  # cria uma lista

item = input("Entre com o item que deseja comprar: ")  # lê uma string

if item in lista:  # se o item estiver na lista

    print("Item disponível")  # imprime a mensagem

else:  # senão
    
        print("Item indisponível")  # imprime a mensagem
# %%
