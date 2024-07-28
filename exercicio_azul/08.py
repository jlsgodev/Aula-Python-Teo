#Faça um programa que receba 4 alturas, armazene em uma lista e 
# depois mostre a soma dessas alturas.

# %%
alturas = []
altura = float(input("Digite a primeira altura: "))
alturas.append(altura)
altura = float(input("Digite a segunda altura: "))
alturas.append(altura)
altura = float(input("Digite a terceira altura: "))
alturas.append(altura)
altura = float(input("Digite a quarta altura: "))
alturas.append(altura)
print(alturas)
print(sum(alturas))


# outro jeito de fazer
# %%
a1 = int(input("entre com a altura em cm: "))
a2 = int(input("entre com a altura em cm: "))
a3 = int(input("entre com a altura em cm: "))
a4 = int(input("entre com a altura em cm: "))

alturas = [a1, a2, a3, a4]

soma = sum(alturas)
print(soma)


# %%

# outro jeito de fazer usando for

alturas = []
for i in range(4):
    altura = float(input("Digite a altura: "))
    alturas.append(altura)
print(alturas)
print(sum(alturas))



# %%


# outro jeito de fazer usando for

alturas = []
for i in range(4):  # 4 é a quantidade de alturas que eu quero receber, começa do 0 e vai até 3
    a = int(input(f"entre com a altura em cm {i+1} : "))  # i+1 para começar a contar do 1
    alturas.append(a)                               # adiciona a altura na lista
soma = sum(alturas)                         # soma as alturas
print(soma)                     # imprime a soma

# %%
