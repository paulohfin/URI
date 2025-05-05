'''
Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", ela funciona da seguinte maneira:

Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma direção até uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele ressurge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano.

Fiddlesticks quer sua ajuda para saber se de uma certa posição é possível atingir um invasor com sua habilidade ultimate.

Obs: Considere que Fiddlesticks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na direção contrária a Fiddlesticks, em velocidade constante.



Entrada
A entrada é composta de várias linhas, cada linha contém os seguintes valores inteiros: Xf, Yf, Xi, Yi, Vi, R1 e R2(0 ≤ Xf, Yf, Xi, Yi, Vi, R1 e R2 ≤ 100), representando respectivamente as coordenadas de Fiddlesticks, as coordenadas iniciais do invasor, a velocidade do invasor, o raio de conjuração da ultimate e o raio de voo dos corvos. Considere a unidade de medida como sendo o metro.

Saída
Na saída você deve imprimir para cada linha o caractere 'Y' caso seja possível atingir o invasor ou 'N' caso contrário, ambos seguidos de uma quebra de linha.
'''
import math

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = map(int, input().split(' '))
        
        if math.sqrt((xf - xi) * (xf - xi) + (yf - yi) * (yf - yi)) + 1.5 * vi <= r1 + r2:
            print('Y')
        else:
            print('N')
    except EOFError:
        break
