def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
for i in range(20):
#declarar em range a posição do números da sequencia para ser printado
    print(fibonacci(i))