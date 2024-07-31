# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos. Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53


segundos = int(input("Digite o número de segundos: ")) # Recebe um número em  segundos
horas = segundos // 3600 # 3600 é o número de segundos em uma hora
segundos = segundos % 3600  # % é o operador de módulo, que retorna o resto da divisão
minutos = segundos // 60    # 60 é o número de segundos em um minuto
segundos = segundos % 60    # % é o operador de módulo, que retorna o resto da divisão

print(horas, ":", minutos, ":", segundos)    # Imprime o resultado em horas, minutos e segundos

# O programa recebe um número em segundos, e converte esse número para horas, minutos e segundos. Para isso, ele divide o número de segundos por 3600, que é o número de segundos em uma hora, e armazena o resultado em horas. Em seguida, ele pega o resto da divisão do número de segundos por 3600, e armazena esse valor em segundos. Depois, ele divide o número de segundos por 60, que é o número de segundos em um minuto, e armazena o resultado em minutos. Por fim, ele pega o resto da divisão do número de segundos por 60, e armazena esse valor em segundos. Por fim, ele imprime o resultado em horas, minutos e segundos.

