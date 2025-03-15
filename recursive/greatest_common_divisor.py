# greatest common divisor

def common(a,b,c=2,son=1):
    if c > min(a,b):
        return son
    if a%c==0 and b%c==0:
        son=c
    return common(a,b,c+1,son)

print(common(4,8))
