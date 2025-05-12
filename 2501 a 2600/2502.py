'''
A cifra mais antiga conhecida é a Cifra de César. César escrevia suas cartas trocando cada letra pela próxima do alfabeto, para evitar que, quando a carta fosse interceptada, conseguissem ler. Com o tempo, a criptografia adquiriu melhor qualidade, mas a criptografia por substituição ainda é uma brincadeira de criança interessante, por exemplo:

ZEN I T
POLAR

Neste tipo de brincadeira, ao escrever uma carta a letra Z é trocada pela letra P e vice versa, bem como: E e O e assim sucessivamente. A frase cifrada desta forma: "Osro roxre osri caftide" pode ser decifrada como: "Este texto esta cifrado". Como a brincadeira ficou séria, a você foi solicitado um programa que decifre as mensagens cifradas a partir de uma chave fornecida.

Entrada
A entrada contém vários casos de teste. Cada caso de teste começa com uma linha indicando dois números inteiros C e N, 0 < C < 21 e 0 < N < 100. C é o tamanho da cifra. Nas duas linhas seguintes está a cifra de tamanho C indicando quais caracteres da primeira linha será substituído por caracteres da segunda linha, um caracter aparece uma única vez, na primeira ou na segunda linha.

A cifra pode conter letras de ‘A’ a ‘Z’, números de ‘0’ a ‘9’ além do espaço em branco e alguns símbolos de pontuação: '.' ',' ';' ':' '(' ')' '!' e '?'. Nas próximas N linhas estão frases e sentenças criptografadas pela cifra fornecida, que você deve decifrar. Cada linha contém no mínimo 1 e no máximo 1000 caracteres. São permitidos quaisquer caracteres ASCII (não extendido) imprimíveis, neste caso não estão presentes nenhum caracter acentuado, nem mesmo 'ç'.

Saída
Para cada caso de teste da entrada seu programa deve gerar para cada linha de frase e sentença de entrada, uma linha com a saída decifrada, respeitando a capitalização da letra (letras maiúsculas são decifradas como maiúsculas e minúsculas como minúsculas quando for possível aplicar a diferenciação, se não for possível serão decifrados como letras minúsculas). Após cada caso de teste deve ser impressa uma linha em branco, inclusive após o último.
'''
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
