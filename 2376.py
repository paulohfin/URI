def venc(t1, t2, p):
    if int(p[0]) > int(p[1]):
        return t1
    else:
        return t2

while True:
    try:
        times = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
        qua = []
        se = []
        fi = []
        for i in range(8):
            v = input().split(' ')
            qua.append(venc(times[2 * i], times[2 * i + 1], v))
        for i in range(4):
            v = input().split(' ')
            se.append(venc(qua[2 * i], qua[2 * i + 1], v))
        for i in range(2):
            v = input().split(' ')
            fi.append(venc(se[2 * i], se[2 * i + 1], v))
        v = input().split(' ')
        print(venc(fi[0], fi[1], v))
    except EOFError:
        break 