# # 1 
# print("Bom dia!")



# #2
# print("Bom dia! Qual seu nome?")
# nome = input()
# print("E um prazer te conhecer " + nome + "!")


#Programa que dá bom dia
def bom_dia():
    print("Bom dia!")

bom_dia()

#Programa que dá bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela
def cumprimentar():
    print("Bom dia!")
    nome = input("Qual é o seu nome? ")
    print(f"É um prazer conhecer você, {nome}!")

cumprimentar()

#Programa que conta uma história simples, parando a cada parágrafo
def contar_historia():
    historia = [
        "Era uma vez, em uma terra distante, um pequeno vilarejo escondido entre montanhas majestosas.",
        "Nesse vilarejo, vivia um jovem chamado João, que sonhava em explorar o mundo além das montanhas.",
        "Um dia, João decidiu partir em uma grande aventura, levando apenas uma mochila e seu corajoso cachorro, Rex.",
        "Eles atravessaram florestas densas e rios turbulentos, enfrentando muitos desafios pelo caminho.",
        "Finalmente, após muitos dias de viagem, eles encontraram um tesouro escondido que mudou suas vidas para sempre."
    ]

    for paragrafo in historia:
        print(paragrafo)
        input("Pressione Enter para continuar...")

contar_historia()



#Programa que calcula a raiz quadrada de um número
import math

def calcular_raiz_quadrada():
    numero = float(input("Digite um número: "))
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

calcular_raiz_quadrada()


#Programa que exibe o dobro de um número inserido pelo usuário
def calcular_dobro():
    numero = float(input("Digite um número: "))
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")

calcular_dobro()
