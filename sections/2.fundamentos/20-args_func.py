def full_name(first_name, last_name):
    print(f"Nome é: {first_name} {last_name}")
    
full_name("Fulano", "Sicrano")

def sum_numbers(a, b):
    return a + b

print(f"Soma é: {sum_numbers(10, 50)}")

def address(country = "Brasil"):
    print(f"Eu moro em: {country}")
    
address()
address("Portugal")
