n = int(input())
temp = n
a1 = int(n / 100)
n -= a1 * 100

a2 = int(n / 50)
n -= a2 * 50

a3 = int(n / 20)
n -= a3 * 20

a4 = int(n / 10)
n -= a4 * 10

a5 = int(n / 5)
n -= a5 * 5

a6 = int(n / 2)
n -= a6 * 2

a7 = int(n)
print(temp)
print(a1,'nota(s) de R$ 100,00')
print(a2,'nota(s) de R$ 50,00')
print(a3,'nota(s) de R$ 20,00')
print(a4,'nota(s) de R$ 10,00')
print(a5,'nota(s) de R$ 5,00')
print(a6,'nota(s) de R$ 2,00')
print(a7,'nota(s) de R$ 1,00')