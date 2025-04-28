while True:
    try:
        n = input()
        bit = 0
        for i in range(len(n)):
            if n[i] == '1':
                bit += 1
        if bit%2 != 0:
            print(n + '1')
        else:
            print(n + '0')
    except EOFError:
        break