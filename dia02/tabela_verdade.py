# Numeros
# 1
# 10.0
# -5 
# -7.54


# Booleanos                # Verdadeiro ou Falso  
# True
# False

# True = 1                  # verdadeiro = 1
# False = 0                 # falso = 0

# and = *                   # multiplicação                 # quando as duas entradas são verdadeiras
# or = +                    # adição                        # quando pelo menos uma das entradas é verdadeira   
# not = ~                   # negação                       # inverte o valor da entrada
# xor = ^                   # ou exclusivo                  # quando as entradas são diferentes
# nand = ~*                 # negação da multiplicação      #  quando pelo menos uma das entradas é falsa
# nor = ~+                  # negação da adição             # quando as duas entradas são falsas
# xnor = ~^                 # negação do ou exclusivo       # quando as entradas são iguais
# implica = ->              # implica                       # quando a primeira entrada é verdadeira e a segunda é falsa
# bi-implica = <->          # bi-implica                    # quando as entradas são iguais
# not implica = ~->         # negação do implica            # quando a primeira entrada é falsa ou a segunda é verdadeira
# not bi-implica = ~<-      # negação do bi-implica         # quando as entradas são diferentes
# not xor = ~^              # negação do ou exclusivo       # quando as entradas são iguais    
# not nand = ~*             # negação da multiplicação      # quando as duas entradas são verdadeiras    
# not nor = ~+              # negação da adição             # quando pelo menos uma das entradas é verdadeira
# not xnor = ~^             # negação do ou exclusivo       # quando as entradas são diferentes    
# not or = ~+               # negação da adição             # quando as duas entradas são falsas
# not and = ~*              # negação da multiplicação      # quando pelo menos uma das entradas é falsa



# modelo tabela verdade and   #Quando as duas entradas são verdadeiras o resultado é verdadeiro  e quando pelo menos uma das entradas é falsa o resultado é falso
# True and True = True             # 1 * 1 = 1
# True and False = False           # 1 * 0 = 0 
# False and True = False           # 0 * 1 = 0  
# False and False = False          # 0 * 0 = 0

# modelo tabela verdade or    # quando pelo menos uma das entradas é verdadeira o resultado é verdadeiro
# True or True = True       # 1 + 1 = 1       
# True or False = True      # 1 + 0 = 1 
# False or True = True      # 0 + 1 = 1
# False or False = False    # 0 + 0 = 0

# modelo tabela verdade not     # quando a entrada é verdadeira o resultado é falso e quando a entrada é falsa o resultado é verdadeiro
# not True = False      # not 1 = 0
# not False = True      # not 0 = 1

# modelo tabela verdade xor  # quando as entradas são diferentes o resultado é verdadeiro e quando as entradas são iguais o resultado é falso
# True xor True = False         # 1 ^ 1 = 0
# True xor False = True         # 1 ^ 0 = 1 
# False xor True = True         # 0 ^ 1 = 1 
# False xor False = False       # 0 ^ 0 = 0

# modelo tabela verdade nand  #quantdo pelo menos uma das entradas é falsa o resultado é verdadeiro e quando as duas entradas são verdadeiras o resultado é falso
# True nand True = False            # 1 * 1 = 1
# True nand False = True            # 1 * 0 = 0
# False nand True = True            # 0 * 1 = 0
# False nand False = True           # 0 * 0 = 0 

# modelo tabela verdade nor  # quando as duas entradas são falsas o resultado é verdadeiro e quando pelo menos uma das entradas é verdadeira o resultado é falso 
# True nor True = False         # 1 + 1 = 1
# True nor False = False        # 1 + 0 = 0    
# False nor True = False        # 0 + 1 = 0
# False nor False = True        # 0 + 0 = 1

# modelo tabela verdade xnor        #quando as entradas são iguais o resultado é verdadeiro e quando as entradas são diferentes o resultado é falso 
# True xnor True = True             # 1 ^ 1 = 1
# True xnor False = False           # 1 ^ 0 = 0    
# False xnor True = False           # 0 ^ 1 = 0
# False xnor False = True           # 0 ^ 0 = 1

# modelo tabela verdade implica   #quando a primeira entrada é verdadeira e a segunda é falsa o resultado é falso e quando a primeira entrada é falsa o resultado é verdadeiro
# True implica True = True              # True implica True = True
# True implica False = False            # True implica False = False

# modelo tabela verdade bi-implica  #quando as entradas são iguais o resultado é verdadeiro e quando as entradas são diferentes o resultado é falso
# True bi-implica True = True           # 1 bi-implica 1 = 1
# True bi-implica False = False         # 1 bi-implica 0 = 0
# False bi-implica True = False         # 0 bi-implica 1 = 0
# False bi-implica False = True         # 0 bi-implica 0 = 1    

# modelo tabela verdade not implica   #quando a primeira entrada é falsa ou a segunda é verdadeira o resultado é verdadeiro e quando a primeira entrada é verdadeira e a segunda é falsa o resultado é falso
# True not implica True = False             # 1 not implica 1 = 0
# True not implica False = True             # 1 not implica 0 = 1

# modelo tabela verdade not bi-implica          #quando as entradas são diferentes o resultado é verdadeiro e quando as entradas são iguais o resultado é falso 
# True not bi-implica True = False              # 1 not bi-implica 1 = 0
# True not bi-implica False = True              # 1 not bi-implica 0 = 1
# False not bi-implica True = True              # 0 not bi-implica 1 = 1
# False not bi-implica False = False            # 0 not bi-implica 0 = 0

# modelo tabela verdade not xor           #quando as entradas são iguais o resultado é verdadeiro e quando as entradas são diferentes o resultado é falso
# True not xor True = False                 # 1 not xor 1 = 0
# True not xor False = True                 # 1 not xor 0 = 1
# False not xor True = True                 # 0 not xor 1 = 1
# False not xor False = False               # 0 not xor 0 = 0

# modelo tabela verdade not nand     #quando as duas entradas são verdadeiras o resultado é falso e quando pelo menos uma das entradas é falsa o resultado é verdadeiro
# True not nand True = True                 # 1 not nand 1 = 1
# True not nand False = False               # 1 not nand 0 = 0
# False not nand True = False               # 0 not nand 1 = 0
# False not nand False = False              # 0 not nand 0 = 0    

# modelo tabela verdade not nor     #quando as duas entradas são falsas o resultado é falso e quando pelo menos uma das entradas é verdadeira o resultado é verdadeiro
# True not nor True = False                 # 1 not nor 1 = 0
# True not nor False = True                 # 1 not nor 0 = 1
# False not nor True = True                 # 0 not nor 1 = 1
# False not nor False = True                # 0 not nor 0 = 1

# modelo tabela verdade not xnor     #quando as entradas são diferentes o resultado é falso e quando as entradas são iguais o resultado é verdadeiro
# True not xnor True = False                    # 1 not xnor 1 = 0
# True not xnor False = True                    # 1 not xnor 0 = 1
# False not xnor True = True                    # 0 not xnor 1 = 1
# False not xnor False = False                  # 0 not xnor 0 = 0

# modelo tabela verdade not or      #quando as duas entradas são falsas o resultado é verdadeiro e quando pelo menos uma das entradas é verdadeira o resultado é falso
# True not or True = False                  # 1 not or 1 = 0
# True not or False = False                 # 1 not or 0 = 0    
# False not or True = False                 # 0 not or 1 = 0
# False not or False = True                 # 0 not or 0 = 1

# modelo tabela verdade not and     #quando pelo menos uma das entradas é falsa o resultado é verdadeiro e quando as duas entradas são verdadeiras o resultado é falso
# True not and True = False                     # 1 not and 1 = 0
# True not and False = True                     # 1 not and 0 = 1
# False not and True = True                     # 0 not and 1 = 1  
# False not and False = True                    # 0 not and 0 = 1









