filmsList = [
    "Inception", "The Shawshank Redemption",
    "The Dark Kgnith", "Pulp Fiction", "Interstellar"
]

# Tamanho da lista
print(len(filmsList))

# Recuperar um item da lista pelo nome
print(filmsList.index("Interstellar"))

# Adicionar item ao final da lista
print(filmsList.append("The lord of the Rings"))

# Ordenar a lista
print(filmsList.sort())

# Copiar itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# Remove todos os items da lista
filmsCopy.clear()
print(filmsCopy)