movieName = "Top Gun"

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
    muito consagrado na indústria
"""

print(movieName.upper()) # Tudo maisculo
print(movieName.lower()) # Tudo minusculo
print(movieName.capitalize()) # Primeira maiuscula
print(movieName.title()) # Primeira por palavra maiuscula
print(movieName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # Retorna posição de um determinado caractere
print(movieName.find("0")) # conta caracteres
print(movieName.replace("Top", "Matrix")) # Altera string
print(movieDescription.split(','))