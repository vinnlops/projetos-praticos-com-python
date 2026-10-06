filmInception = {
    "title": "Inception",
    "yearRealease": 2010,
    "imbRating": 8.8,
    "genre": ["Action", "Adventure", "Sci-Fi"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# Recuperando valores do dicionário
print(filmInception["genre"])
print(filmInception.get("imbRating"))

# Adicionando novos valores ao dicionário
print(filmInception.keys())

# Recuperando os valores do dicionário
print(filmInception.values())

# Recuperando os itens do dicionário
print(filmInception.items())

# Adicionando novos valores ao dicionário
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# Atualizando valores do dicionário
filmInception.update({"imbRating": 9})
print(filmInception)

# Removendo valores do dicionário
filmInception.pop("yearRealease")
print(filmInception)