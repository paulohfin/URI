while True:
    try:
        n = int(input())
        livro = []
        for i in range(n):
            livro.append(input())
        livro.sort()
        for i in livro:
            print(i)
    except EOFError:
        break