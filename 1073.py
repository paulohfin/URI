n = int(input())

for i in range(2, n + 1):
    if i % 2 == 0:
        print(str(i) + "^2 = " + str(i * i))