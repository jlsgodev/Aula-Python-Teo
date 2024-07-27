#Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago


tipo_sorvete = input("Qual tipo de sorvete você deseja? [casquinha/cascão/cestinha]: ")
sabor = input("Qual sabor você deseja? [morango/creme/chocolate]: ")
cobertura = input("Qual cobertura você deseja? [caramelo/morango/chocolate/sem]: ")

valor = 0
if tipo_sorvete == "casquinha":
    valor += 1.00

elif tipo_sorvete == "cascão":
    valor += 2.50

elif tipo_sorvete == "cestinha":
    valor += 4.00

else:
    print("Faça uma escolha válida!")

if cobertura == "caramelo" or cobertura == "morango" or cobertura == "chocolate": # na mesma linha para economizar espaço e facilitar a leitura
    valor += 1.50

elif cobertura == "sem":
    valor += 0.00

else:
    print("Faça uma escolha válida!")

print("Seu sorvete", tipo_sorvete, "de" , sabor, "cobertura", cobertura, "custa R$", valor )  #adiciona , sabor e , cobertura para mostrar o sabor e a cobertura escolhida
