arr = [10, 15, 3, 7]

def function(value):
    # Checking if the input number can be obtained as a combination of those of the array
    for x in arr:
        if ( value - x ) in arr:
            return True
    
    return False

if function(22):
    print("True - The value can be obtained as a combination of two numbers of the array")
else:
    print("False - The value canot be obtained as a combination of two numbers of the array") 
