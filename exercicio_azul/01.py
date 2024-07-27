# Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

print("Bem vindo a nossa loja de água!")
escolha = input("Você deseja água mineral ou com gás? [mineral/gas]: ")

if escolha == "mineral":
    print("O valor da sua compra é R$1,50")

elif escolha == "gas":
    print("O valor da sua compra é R$2,50")
else:
    print("Faça uma escolha válida!")


