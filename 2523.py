while True:
    try:
        letra = input()
        n = int(input())
        k = input().split(' ')
        for i in k:
            print(letra[int(i) - 1],end='')
        print()
    except EOFError:
        break 