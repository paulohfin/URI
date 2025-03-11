n = int(input())
 
while n != 0:
    antigo = 100000000000000000000000000000000
    nome = ''
    for i in range(n):
        leitura = input()
        nome2, ano, tempo = leitura.split(' ')
        if antigo > int(ano) - int(tempo):
            nome = nome2
            antigo = int(ano) - int(tempo)
            
    print(nome)
    
    n = int(input())
