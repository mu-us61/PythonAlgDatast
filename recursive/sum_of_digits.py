def sumofdigits(n):
    assert n>0 and int(n) == n, "yanlis veri"
    if n < 10 :
        return n
    return int(str(n)[-1]) + sumofdigits(n//10)

print(sumofdigits(1233255))
