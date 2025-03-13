resp = int(input())

linha = input().split(' ')
cont = 0
for i in linha:
    if i == str(resp):
        cont += 1
print(cont)