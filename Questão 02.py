# Define o número a ser verificado
num = int(input("Digite um número: "))

# Inicia a sequência de Fibonacci com os dois primeiros valores
fibonacci = [0, 1]

# Calcula a sequência de Fibonacci até encontrar um número maior ou igual ao número informado
while fibonacci[-1] < num:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

# Verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")