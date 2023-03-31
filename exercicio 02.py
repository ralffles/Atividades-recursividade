def print_fatorial(n, resultado=1):
    if n == 0:
        return
    else:
        resultado *= n
        print(resultado)
        print_fatorial(n-1, resultado)
print_fatorial (6)