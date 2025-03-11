n = int(input())

linha = input().split(' ')
for i in linha:
    res = int(i,16)
    print(chr(res), end='')
print()