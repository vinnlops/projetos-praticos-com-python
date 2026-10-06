def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7,9)
sum(7,9,10,11)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
        
print("Lista de Cursos:")
presentation(name="Python", category="backend", level="Iniciante")