n = int(input())
ano = int(n / 365)
n -= ano*365
mes = int(n / 30)
n -= mes*30

print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(n, 'dia(s)')