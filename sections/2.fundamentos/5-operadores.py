n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))

sum = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
mod = n1 % n2
exp = n1 ** n2

print(f"Potencia do numero {n1} por {n2} é {exp}")
print(f"Resto da divisão de {n1} por {n2} é {exp}")

# Comparação
bigger = n1 > n2
smaller = n1 < n2
equal = n1 == n2
different = n1 != n2
bigger_equal = n1 >= n2
smaller_equal = n1 <= n2

print(f"Os numero {n1} e {n2} são iguais? {equal}")
print(f"{n1} menor que {n2}? {smaller}")

# Atribuição
n1 += 1
n1 *= 1
n1 /= 1
n1 -= 1