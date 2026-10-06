moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

for movie in moviesList:
    print(movie)

for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)
    
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else: 
    average = 0
    
print(f"Média de avaliação do filme {movieName} é: {average:.2f}")