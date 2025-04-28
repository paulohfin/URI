while True:
    try:
        a, b = map(int, input().split(' '))
        
        a = str(bin(a))
        b = str(bin(b))
        i = len(a) - 1 
        j = len(b) - 1 
        m = 1
        soma = 0
        while i > 1 and j > 1:
            if int(a[i]) + int(b[j]) == 1:
                soma += m
            i -= 1 
            j -= 1 
            m *= 2
        while i > 1:
            soma += m 
            i -= 1
            m *= 2
        while j > 1:
            soma += m 
            j -= 1
            m *= 2
        print(soma)
    except EOFError:
        break 