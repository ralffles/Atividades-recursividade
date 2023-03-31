def sm(x):
    if x < 10:
        return x
    else:
        return (x % 10) + sm(x // 10)
print(sm(145))
