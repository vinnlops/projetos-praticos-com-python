filmsTuple = (
    "Inception", "The Shawshank Redemption",
    "The Dark Knight", "Pulp Fiction", "Interstellar"
)
print(type(filmsTuple))

# Buscar os dois primeiros itens da tupla
print(filmsTuple[0:2])

# buscar o ultimo item da tupla
print(filmsTuple[-1])

# Buscar filme até uma determinada posição
print(filmsTuple[:3])

# Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# Buscar filmes pelo nome
print(filmsTuple.index("Pulp Fiction"))