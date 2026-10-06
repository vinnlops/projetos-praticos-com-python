movieName = "Top Gun"

# string[inicio:fum] - indice começa na posição 0 | indice final - 1

# 1 - Busca toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a ultima posição
print(movieName[:5])

# 3 - Buscar toda a string da terceira até a ultima posição
print(movieName[2:])

"""
string[inicio:fim:passo]
indice começa na posição 0 | indice final - 1
passo - determina o incremento. Por padrão esse numero é 1.
"""

# 4 - Buscar toda string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos indices impares
print(movieName[1::2])

# 6 - Inverter uma string de tras para frente
print(movieName[::-1])