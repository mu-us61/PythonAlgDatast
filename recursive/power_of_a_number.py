# calculate power of a number

def powOfNumber(number,power):
    assert isinstance(number, int) and isinstance(power, int) and power >= 0, "Inputs must be integers, and power must be non-negative."
    if power==0:
        return 1
    return number*powOfNumber(number,power-1)


print(powOfNumber(-2,4))
    
