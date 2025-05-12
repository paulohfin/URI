'''
Dois times, Cormengo e Flaminthians, participam de um campeonato de futebol, juntamente com outros times. Cada vitória conta três pontos, cada empate um ponto. Fica melhor classificado no campeonato um time que tenha mais pontos. Em caso de empate no número de pontos, fica melhor classificado o time que tiver maior saldo de gols. Se o número de pontos e o saldo de gols forem os mesmos para os dois times então os dois times estão empatados no campeonato.

Dados os números de vitórias e empates, e os saldos de gols dos dois times, sua tarefa é determinar qual dos dois está melhor classificado, ou se eles estão empatados no campeonato.

Entrada
A entrada é descrita em uma única linha, que contém seis inteiros, separados por um espaço em branco: Cv, Ce, Cs, Fv, Fe e Fs, (0 ≤ Cv, Ce, Fv, Fe ≤ 100), (-1000 ≤ Cs, Fs ≤ 1000) que são, respectivamente, o número de vitórias do Cormengo, o número de empates do Cormengo, o saldo de gols do Cormengo, o número de vitórias do Flaminthians, o número de empates do Flaminthians e o saldo de gols do Flaminthians.

Saída
Seu programa deve imprimir uma única linha. Se Cormengo é melhor classificado que Flaminthians, a linha deve conter apenas a letra 'C', se Flaminthians é melhor classificado que Cormengo, a linha deve conter apenas a letra 'F', e se os dois times estão empatados a linha deve conter apenas o caractere '='.
'''

while True:
    try:
        cv, ce, cs, fv, fe, fs = map(int, input().split(' '))
        
        Cs = 3 * cv + ce 
        Fs = 3 * fv + fe 
        
        if Cs > Fs:
            print('C')
        elif Cs < fs:
            print('F')
        elif cs > fs:
            print('C')
        elif fs > cs:
            print('F')
        else:
            print('=')
    except EOFError:
        break
