'''
Estamos no ano 2030. Os benefícios da mecânica quântica já são bastante conhecidos e a computação foi e está sendo fortemente modificada em razão das recentes descobertas. Dessa forma, quase todos os computadores e smartphones estão bem diferentes de como eram em 2016 (há 14 anos atrás). Em razão da importância e da imensurável aplicabilidade desse ramo da física no cotidiano, a maioria dos países determinou que os princípios do mesmo devem ser ensinados no último ano do ensino médio.

Maria está concluindo o ensino médio e faz parte da primeira turma que contém a mecânica quântica na grade curricular. As primeiras aulas desse conteúdo já foram ministradas e Maria está estudando para a prova, que será na próxima semana. O conteúdo cobrado na avaliação será: O Princípio da Incerteza e a Superposição dos elétrons.

Você, como bom programador(a) e amigo(a) de Maria, decidiu ajudá-la escrevendo um algoritmo que seja capaz de contar quantos ciclos completos conterá cada experimento que será realizado com elétrons. Sabe-se, pelo princípio da incerteza, que uma característica não interfere em outra como, por exemplo, a cor apresentada por um determinado elétron não implica em sua dureza ou maleabilidade. Você vai considerar que os experimentos começam sempre com a determinação da cor e em seguida com a determinação da dureza, esse processo pode se repetir dependendo de quantas etapas Maria queira que o experimento possua.

Supondo que ela escolheu 3 etapas, o experimento seria realizado da seguinte forma:

Determinação da cor → Determinação da dureza → Determinação da cor

Seu programa deve informar quantos ciclos completos foram realizados, sabendo-se que, para Maria, um ciclo completo é composto pela determinação da cor e da dureza do elétron, respectivamente. No caso de teste apresentado acima, seria 1 ciclo completo. Mas se ela escolhesse 4 etapas, seriam 2 ciclos completos.

Entrada
A entrada é composta por diversos casos de teste. Cada caso de teste é composto por um único inteiro N, que representa a quantidade de etapas que Maria deseja que o experimento completo possua (-1 <= N <= 1000). É importante lembrar que uma etapa pode ser a determinação da cor ou da dureza, enquanto um ciclo é composto pela determinação das duas características. O programa se encerra com N = -1.

Saída
Para cada N informado por Maria deve ser retornada uma única linha contendo o resultado no seguinte formato: Experiment X: Y full cycle(s). Em que X representa o número do caso de teste e Y representa o número de ciclos completos.
'''
n = int(input())
cont = 0
while n != -1:
    cont += 1
    print('Experiment ' + str(cont) + ': ' + str(int(n / 2)) + ' full cycle(s)')
    
    n = int(input())
