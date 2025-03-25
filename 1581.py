n = int(input())
for i in range(n):
    m = int(input())
    idioma = ''
    for j in range(m):
        idi = input()
        if idioma == '':
            idioma = idi 
        elif idi != idioma:
            idioma = 'ingles'
    print(idioma)