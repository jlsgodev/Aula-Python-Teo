idade =  int(input("Digite a sua idade: "))
if idade <= 18:  # se for menor ou igual a 18 anos de idade
    print("Você é menor de idade!")
    print("Va para a casa beber leite!")

elif idade > 90:  # se for maior que 90 anos de idade
    print("Você é idoso!")
    print("Beba com moderação!")

else:  # se não for menor de idade
    print("Você é maior de idade")
    print("Beba a vontade!")






# outra opcao de codigo para o mesmo problema acima 
if 18  <= idade <= 90:  # se esta entre 18 e 90 anos de idade 
    print("Você é maior de idade") # imprime a mensagem
    print("Beba a vontade!") # imprime a mensagem

elif idade >= 90:
    print("Você é idoso!")
    print("Beba com moderação!")

else:
    print("Você é menor de idade!")
    print("Va para a casa beber leite!")    