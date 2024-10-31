# recursion fibonacci

def stairs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return stairs(n-1) + stairs(n-2)

# 8
print(stairs(5))