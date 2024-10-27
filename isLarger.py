# recursion to find if a is larger than b

def isLarger(a, b):
    if a == b:
        return False
    if a == 0:
        return False
    if b == 0:
        return True
    # decrement a and b, whichever reaches 0 first will determine who is larger
    # example: a=2 b=1 -> a=1 b=0, a > b 
    return isLarger(a-1, b-1)

# True
print(isLarger(2, 1))

# False
print(isLarger(1, 2))