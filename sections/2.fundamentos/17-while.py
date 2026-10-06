moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    
    print(moviesList[index])
    index += 1
    
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        continue
    
    print(moviesList[index])
    index += 1