# %%

minha_lista = []                    # cria uma lista vazia
print(minha_lista)              # imprime a lista vazia


# %%

minha_lista = ["jhon", 'goncalves', 32, 1.79, 82.00]        # cria uma lista com 5 elementos
print(minha_lista)                  # imprime a lista

# %%
minha_lista[0]                  # acessa o primeiro elemento da lista


# %%
minha_lista[1]                  # acessa o segundo elemento da lista

# %%
minha_lista[-1]             # acessa o último elemento da lista


# %%
minha_lista[:2]             # acessa os dois primeiros elementos da lista

# %%
minha_lista[-2:]            # acessa os dois últimos elementos da lista


# %%

nova_lista = minha_lista[:]   # cria uma cópia da lista
print(nova_lista)

# %%
minha_lista[::-1] # acessa todos os elementos da lista de trás para frente

# %%

minha_lista[::2]        # acessa todos os elementos da lista de 2 em 2

# %%

notas = []                 # cria uma lista vazia
nota = 7.75               # cria uma variável com um valor
notas.append(nota)      # adiciona um elemento à lista
print(notas)            # imprime a lista

notas.append(10)        # adiciona um elemento à lista
print(notas)            # imprime a lista com dois elementos adicionados 

notas.extend([5.75, 6.24]) # .extend estende a lista, []permite adicionar mais de um elemento
print(notas)            # imprime a lista com dois elementos adicionados    

notas = notas + [10, 9.25]     # concatena uma lista com outra lista 
print(notas)

# %%
notas.remove(10)        # remove o elemento 10 da lista, somente a primeira ocorrência
print(notas)            # imprime a lista sem o elemento


# %%
notas[2]                # acessa o terceiro elemento da lista

# %%
nome = "jhon"               # cria uma variável com um valor
nome_alto = nome.upper()     # converte o nome para maiúsculo
print(nome_alto)            # imprime o nome em maiúsculo

# %%


nomes = ["jhon", "evandra", "leon", "haku"]  # cria uma lista com 4 elementos
for nome in nomes:             # para cada nome na lista 
    print( nome.title())   # imprime o nome com a primeira letra em maiúsculo
nomes.append("heitor") # .append adiciona um elemento à lista com append 
print(nomes)
nomes.extend(["isabely", "dai", "michel"]) # adiciona varios elemento à lista com extend
print(nomes)
# %%


dados = ["jhon", "goncalves", 32, ["geromel", "kaneman", "cortez", "lucas"]]  # cria uma lista com 7 elementos

dados[3] [-1] # acessa o último elemento da lista que está dentro da lista. encadeando a indexação
# %%
j