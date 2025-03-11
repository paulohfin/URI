n = int(input())
cont = 0
while n != -1:
    cont += 1
    print('Experiment ' + str(cont) + ': ' + str(int(n / 2)) + ' full cycle(s)')
    
    n = int(input())