par = []
impar = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for i in range(len(par)):
            print('par[' + str(i) + '] = ' + str(par[i]))
        par = []
    
    if len(impar) == 5:
        for i in range(len(impar)):
            print('impar[' + str(i) + '] = ' + str(impar[i]))
        impar = []

for i in range(len(impar)):
    print('impar[' + str(i) + '] = ' + str(impar[i]))
for i in range(len(par)):
    print('par[' + str(i) + '] = ' + str(par[i]))