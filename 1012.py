a1, a2, a3 = map(float, input().split(' '))

print(f'TRIANGULO: %0.3f' %(a1 * a3 / 2))
print(f'CIRCULO: %0.3f' %(3.14159 * a3 * a3))
print(f'TRAPEZIO: %0.3f' %((a1 + a2) * a3 / 2))
print(f'QUADRADO: %0.3f' %(a2 * a2))
print(f'RETANGULO: %0.3f' %(a1 * a2))