# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água





print("Bem vindo a nossa loja de água!")
escolha = input("Você deseja água mineral ou com gás? [mineral/gas]: ")

quantidade = int(input("Quantas garrafas você deseja? "))
total = 0
if escolha == "mineral":
    total = 1.50 * quantidade 

elif escolha == "gas":
    total = 2.50 * quantidade
else:
    print("Faça uma escolha válida!")

print(f"O valor da sua compra é R${total:.2f}")

