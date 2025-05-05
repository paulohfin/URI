while True:
    try:
        c, n = map(int, input().split(' '))
        p1 = input()
        p2 = input()
        dic = {}
        for i in range(len(p1)):
            dic[p1[i].lower()] = p2[i].lower()
            dic[p2[i].lower()] = p1[i].lower()
            
        for i in range(n):
            l = input()
            
            for j in range(len(l)):
                k = None
                try: k = dic[l[j].lower()]
                except KeyError:
                    k = None
                if k is not None:
                    if l[j].isupper():
                        print(k.upper(),end='')
                    else:
                        print(k,end='')
                else:
                    print(l[j],end='')
            print('')
        print()
    except EOFError: