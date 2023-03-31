def pot(a,b):
    if b == 0:
        return 1
    else:
        return a * pot(a,b-1)
print(pot(10,5))