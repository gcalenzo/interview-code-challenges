arr = [3, 4, -1, 1, 2, 6, 7]

def function():
    x = 1
    while x <= (max(arr) + 1):
        if not x in arr:
            return x
        x += 1

print("The first missing positive integer is ", function())