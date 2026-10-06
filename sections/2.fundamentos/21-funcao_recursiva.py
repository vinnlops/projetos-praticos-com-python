def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
number = int(input("Digite o numero para o fatorial:\n"))
print(f"O fatorial de {number} é {factorial(number)}")
