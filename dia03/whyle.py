# %%
# Exemplo de uso do laço de repetição while em Python 
qtde = int(input("Quantos fodases você quer? ")) # recebe o numero de fodases que o usuário quer
count = 1               # inicia a contagem em 1
while count <= qtde:    # enquanto a contagem for menor ou igual ao número de fodases que o usuário quer
    print("Fodase!")    # imprime "Fodase!" 
    count += 1          # incrementa a contagem em 1
# %%


while True:
    senha = input("Digite a senha: ") # recebe a senha do usuário
    if senha == "fodase":        # se a senha for "fodase"
        break                    # sai do laço de repetição usando o comando break 

    elif senha == "12345678":       # dica que a senha  esta proxina de acertar
        print("Quase...")           # ao final do laço, imprime "Quase..." se a senha for "12345678" e depois volta ao início do laço

    else:                         # senão
        print("Fodase!")    # imprime "Fodase!"
print("Saí! Porra!") # imprime "Saí! Porra!" quando a senha for "fodase"

# %%



contador = 1            # inicia a contagem em 1
while contador <= 15:   # enquanto a contagem for menor ou igual a 15

    if contador % 2 == 0:   # se o contador for par (o resto da divisão por 2 é zero)  
        print(contador)     # imprime o contador

    contador += 1           # incrementa a contagem em 1 


# %%

