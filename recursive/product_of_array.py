def productArray (arr):
    if len(arr)==0:
        return 1
    return arr[0] * productArray(arr[1:])

print(productArray([1,2,3]))
