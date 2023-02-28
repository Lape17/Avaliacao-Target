string = input("Digite uma string: ")

inverso = []

for i in range(len(string) - 1, -1, -1):
    inverso.append(string[i])

inverso_string = "".join(inverso)

print(f"A string invertida é: {inverso_string}")