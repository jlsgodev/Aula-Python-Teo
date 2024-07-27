# Exemplos de Tabela Verdade
#%%
# True = 1  False = 0    # True e False são valores booleanos  # 1 e 0 são valores inteiros  
 
# and
print("True e True=", bool(1 * 1))
print("True e False=", bool(1 * 0))
print("False e True=", bool(0 * 1))
print("False e False=", bool(0 * 0))

# or
print("True ou True=", bool(1 + 1))
print("True ou False=", bool(1 + 0))
print("False ou True=", bool(0 + 1))
print("False ou False=", bool(0 + 0))

# xor "ou, mas não ambos"
print("True xor True=", bool(1 ^ 1))
print("True xor False=", bool(1 ^ 0))
print("False xor True=", bool(0 ^ 1))
print("False xor False=", bool(0 ^ 0))

# nand "não e"
print("True nand True=", bool(not(1 * 1)))
print("True nand False=", bool(not(1 * 0)))
print("False nand True=", bool(not(0 * 1)))
print("False nand False=", bool(not(0 * 0)))

# nor "não ou"
print("True nor True=", bool(not(1 + 1)))
print("True nor False=", bool(not(1 + 0)))
print("False nor True=", bool(not(0 + 1)))
print("False nor False=", bool(not(0 + 0)))
      
# xnor "ou exclusivo ou não"
print("True xnor True=", bool(1 == 1))
print("True xnor False=", bool(1 == 0))
print("False xnor True=", bool(0 == 1))
print("False xnor False=", bool(0 == 0))

# implica "se, então"
print("True implica True=", bool(1 <= 1))
print("True implica False=", bool(1 <= 0))

# bi-implica "se e somente se"
print("True bi-implica True=", bool(1 == 1))
print("True bi-implica False=", bool(1 == 0))
print("False bi-implica True=", bool(0 == 1))
print("False bi-implica False=", bool(0 == 0))

# not implica "não implica"
print("True not implica True=", bool(not(1 <= 1)))
print("True not implica False=", bool(not(1 <= 0)))
      
# not bi-implica "não bi-implica"
print("True not bi-implica True=", bool(not(1 == 1)))
print("True not bi-implica False=", bool(not(1 == 0)))
print("False not bi-implica True=", bool(not(0 == 1)))
print("False not bi-implica False=", bool(not(0 == 0)))

# not xor "não ou exclusivo"
print("True not xor True=", bool(not(1 ^ 1)))
print("True not xor False=", bool(not(1 ^ 0)))
print("False not xor True=", bool(not(0 ^ 1)))
print("False not xor False=", bool(not(0 ^ 0)))

# not nand "não nand"
print("True not nand True=", bool(not(not(1 * 1))))
print("True not nand False=", bool(not(not(1 * 0))))
print("False not nand True=", bool(not(not(0 * 1))))
print("False not nand False=", bool(not(not(0 * 0))))
      
# not nor "não nor"
print("True not nor True=", bool(not(not(1 + 1))))
print("True not nor False=", bool(not(not(1 + 0))))
print("False not nor True=", bool(not(not(0 + 1))))
print("False not nor False=", bool(not(not(0 + 0))))



# not xnor "não xnor"
print("True not xnor True=", bool(not(1 == 1)))
print("True not xnor False=", bool(not(1 == 0)))
print("False not xnor True=", bool(not(0 == 1)))
print("False not xnor False=", bool(not(0 == 0)))



      

# %%
