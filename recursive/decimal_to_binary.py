# decimal to binary

def decToBin(n):
    if n ==0:
        return "0"
    if n ==1:
        return "1"
    
    kalan=n%2
    
    return str(decToBin(int(n/2))) + str(kalan)

print(decToBin(5))
