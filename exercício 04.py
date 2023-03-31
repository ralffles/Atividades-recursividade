def mmc(a,b):
    return (a*b)//mdc(a,b)
def mdc(a,b):
    if b==0:
        return a
    else:
        return mdc(b, a%b)
print (mmc(24,16))