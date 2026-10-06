filmsSet = {"The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"}

print(type(filmsSet))

# Buscar o tamanho do set
print(len(filmsSet))

# True e 1 são considerados o mesmo valor em um set
exampleSet = {1, 2, 3, True, False}
print(exampleSet)

exampleSet.update(exampleSet)
print(filmsSet)

filmsSet.remove(2)
print(filmsSet)