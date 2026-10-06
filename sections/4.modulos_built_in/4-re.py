import re

text = "Udemy - uma plataforma com muitos cursos"

match = re.search(r'muitos cursos', text)
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

site = "https://udemy.com"
math = re.search(r'\.', site)
print(match)

pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

rule = r'^A'
phrases= ['A cada esta suja', 'O dia esta lindo', "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não Corresponde: {f}")
        
rule_end = r'!$'
phrase2 = "O dia esta lindo!"
match = re.search(rule_end, phrase2)
if match:
    print("SIm, corresponde")
else:
    print("Não corresponde")