'''
A Internet Computer Parts Company (ICPC) é uma loja on-line que vende peças de computador. Pares de conectores elétricos em linha estão entre as peças mais populares que ICPC vende. No entanto, elas também são uma das peças que são devolvidos com mais freqüência por clientes insatisfeitos, porque devido a erros na embalagem os conectores enviados para os clientes podem não ser compatíveis..

Um conector em-linha é constituído por cinco pontos de ligação, marcadas de 1 a 5. Cada ponto de ligação de um conector pode ser ou um plugue ou uma tomada. Dizemos dois conectores são compatíveis se, para cada rótulo, um ponto de conexão é um plugue e outro ponto de ligação é uma tomada (em outras palavras, dois conectores são compatíveis se, para cada ponto de conexão com o mesmo rótulo, um plugue e uma tomada se encontram quando os dois conectores estão conectados).

A figura abaixo mostra exemplos de dois conectores que são compatíveis e dois conectores que não são compatíveis.



ICPC está introduzindo uma Máquina de Verificação Automártica (ACM) de última geração, com um verificador óptico, que vai verificar se os dois conectores embalados para um cliente são realmente compatíveis. O complexo e caro hardware do ACM está pronto, mas eles precisam de sua ajuda para terminar o software.

Dadas as descrições de um par de conectores em linha, sua tarefa é determinar se os conectores são compatíveis.

Entrada
A primeira linha contém cinco números inteiros Xi (0 ≤ Xi≤ 1 para i = 1, 2,..., 5), que representa os pontos de conexão do primeiro conector do par. A segunda linha contém cinco números inteiros Yi (0 ≤ Yi ≤ 1 para i = 1, 2,..., 5), que representa os pontos de conexão do segundo conector. Na entrada, um 0 representa uma tomada e um 1 representa um plugue.

Saída
Apresente uma linha com um caractere que representa se os conectores são compatíveis ou não. Se eles são compatíveis escrever a letra maiúscula "Y"; caso contrário, escrever a letra maiúscula "N".
'''
p1 = input()
p2 = input()

a1, a2, a3, a4, a5 = map(int, p1.split(' '))
b1, b2, b3, b4, b5 = map(int, p2.split(' '))

if a1 + b1 == 1 and a3 + b3 == 1 and a4 + b4 == 1 and a5 + b5 == 1 and a2 + b2 == 1:
    print('Y')
else:
    print('N')
