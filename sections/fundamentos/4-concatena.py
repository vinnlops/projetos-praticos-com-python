name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

# Alternativa 1
print("Dados do Filme")
print("===================")
print("Nome do filme", name)
print("Ano de lançamento", yearLaunch)
print("Nota do filme", noteMovie)

# Alternativa 2
print("Nome do Filme: ", name, "\nAno de Lançamento: ", yearLaunch, "\nNota do filme: ", noteMovie)

# Alternativa 3
print(f"Nome do filme: {name}\n"
      f"Nome do lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}"
      )