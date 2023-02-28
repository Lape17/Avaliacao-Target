def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


numero = int(input("Informe um número: "))

pertence = False
i = 0

while fibonacci(i) <= numero:
    if fibonacci(i) == numero:
        pertence = True
        break
    i += 1

if pertence:
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")