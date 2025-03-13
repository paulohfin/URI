while True:
    try:
        n = int(input())
        conta = 7
        n -= 10
        if n >= 20:
            conta += 20
        elif n > 0:
            conta += n
        n -= 20
        if n >= 70:
            conta += 140
        elif n > 0:
            conta += 2 * n
        n -= 70
        if n > 0:
            conta += 5 * n
        print(conta)
    except EOFError:
        break