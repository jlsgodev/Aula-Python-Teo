#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
# %%
palavra = input("Entre com uma palavra: ")  # lê uma string

cont = 0  # inicializa o contador

for i in palavra:  # para cada letra em palavra
    if i == "a":   # se a letra for "a"
        cont += 1  # incrementa o contador

print(f"A letra 'a' aparece {cont} vezes na palavra '{palavra}'")  # imprime a mensagem






#  palavra.count("a")             # conta quantas vezes a letra "a" aparece em palavra


# %%
