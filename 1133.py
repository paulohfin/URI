a = int(input())
b = int(input())

if a > b:
    maxi = a
    a = b
    b = maxi

for i in range(a + 1, b):
    if i % 5 == 2 or i % 5 == 3:
        print(i)