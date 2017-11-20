# PROJETO 5 - OPÇÃO B: O ALGORITMO HÚNGARO PARA ALOCAÇÃO DE TAREFAS
O programa deve ler um grafo bipartido a partir de um arquivo e encontrar um emparelhamento máximo se ele existir ou mostrar que ele não existe.

## METODOLOGIA

A implementação deve seguir o algoritmo Húngaro. O programa deve a partir de um emparelhamento inicial dado, obter um emparelhamento máximo M, caso M exista. Se M não existir, o programa deve fornecer como saída o subconjunto de vértices pertencentes a X que ferem a condição do casamento. 

## QUESTIONAMENTOS

### a) Considere um cenário em que empregados são alocados a oportunidades de emprego com base num grafo de compatibilidades. Esse problema é modelado como um grafo bipartido G em que o conjunto X é composto por empregados e o conjunto Y é composto por empresas. Se um candidato x possui requisitos e está apto a assumir um emprego oferecido pela empresa y, então deve haver uma aresta (x,y) em G. Sejam os grafos bipartidos G a seguir.

O grafo em questão tem 10 vértices em X e 10 vértices em Y. Pergunta-se: utilizando um emparelhamento inicial M, é possível encontrar um emparelhamento máximo? Se sim, forneça um emparelhamento máximo. Caso contrário, mostre porque tal emparelhamento não existe.

### i) Na primeira execução considere M inicial dado por: M = {(0,11); (1,13)}

### ii) Execute o método novamente considerando outro emparelhamento inicial diferente do utilizado no item i). Compare os resultados obtidos. Eles são iguais ou diferentes? Em outras palavras, o resultado final depende ou não da inicialização?
