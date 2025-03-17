arr= ["asd","vad","gfdg"]

def capitalize(arr):
    result = []
    if len(arr)==0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    
    return  result + capitalize(arr[1:])
    

print(capitalize(arr))
