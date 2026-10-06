import random

list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))

r1 = random.randint(5, 15)
print(r1)

name = "Curso Python"
r2 = random.choice(name)
print(r2)

print(random.sample(list1, 2))
print(random.sample(list1, 6))

done = False
while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o número")
    print("2. Sair")
    
    choice = input(">")
    if choice == "1":
        print("================ Advinhe o numero de 1 a 10 =================\n")
        number = int(input("Digite um numero de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida, escolha outra")        
    