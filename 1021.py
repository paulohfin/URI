din = float(input())

print("NOTAS:")
print(int(din/100),"nota(s) de R$ 100.00")
din -= int(din/100) * 100

print(int(din/50),"nota(s) de R$ 50.00")
din -= int(din/50) * 50

print(int(din/20),"nota(s) de R$ 20.00")
din -= int(din/20) * 20

print(int(din/10),"nota(s) de R$ 10.00")
din -= int(din/10) * 10

print(int(din/5),"nota(s) de R$ 5.00")
din -= int(din/5) * 5

print(int(din/2),"nota(s) de R$ 2.00")
din -= int(din/2) * 2

print("MOEDAS:")
print(int(din),"moeda(s) de R$ 1.00")
din -= int(din)
din *= 100
print(int(din/50),"moeda(s) de R$ 0.50")
din -= int(din/50) * 50

print(int(din/25),"moeda(s) de R$ 0.25")
din -= int(din/25) * 25

print(int(din/10),"moeda(s) de R$ 0.10")
din -= int(din/10) * 10

print(int(din/5),"moeda(s) de R$ 0.05")
din -= int(din/5) * 5

print(int(din),"moeda(s) de R$ 0.01")
