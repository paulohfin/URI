import math

a, b, c = map(float, input().split(' '))

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    print(f"R1 = %0.5f" %(float((- b + math.sqrt(delta)) / (2 * a))))
    print(f"R2 = %0.5f" %(float((- b - math.sqrt(delta)) / (2 * a))))