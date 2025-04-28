def raiz(n):
    if n > 0:
        return 1/(2+raiz(n-1))
    else: return 0
while True:
    try:
        n = int(input())
        
        print('%.10f' %(1 + raiz(n)))
    except EOFError:
        break