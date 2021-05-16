arrInput = [1, 2, 3, 4, 5]

def function():
    arrOutput = []

    for x in arrInput:
        localSum = 1 
        
        for y in arrInput:
            if not y == x:
                localSum *= y
        
        arrOutput.append(localSum)

    return arrOutput

print("Input array: ",  arrInput)
print("Output array: ", function())