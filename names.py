from faker import Faker
from math import floor

def binarySearch(A, n, T):
    L = 0
    R = n - 1
    while L <= R:
        m = floor((L+R)/2)
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return str(T) + " found at index " + str(m)
    return 0

fake = Faker()

names = []

for i in range(20):
    names.append(fake.name())
    i = i + 1

names.sort()
print(names)
print(len(names))

search = input("Search for name: ")

print(binarySearch(names, len(names), search))
