# o problema da Torre de Hanói é resolvido de forma recursiva porque o movimento de vários discos pode ser dividido em subproblemas menores. A seguir está o código do algoritmo e uma explicação do processo:

def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return

    
    torre_de_hanoi(n - 1, origem, auxiliar, destino)

    
    print(f"Mova o disco {n} de {origem} para {destino}")

    
    torre_de_hanoi(n - 1, auxiliar, destino, origem)


"""
Explicação:

O problema é resolvido seguindo estes passos:

Se houver apenas um disco (caso base), ele é movido diretamente do pino de origem para o pino de destino. Isso resolve o problema para um único disco.

Para mais de um disco, o problema é dividido em três partes:

 Primeiro, os n-1 discos menores são movidos da origem para o pino auxiliar. Isso é feito chamando a função recursivamente.
 Em seguida, o maior disco (disco n) é movido diretamente da origem para o destino.
 Por fim, os n-1 discos que estão no pino auxiliar são movidos para o destino, novamente utilizando a recursão.

 Por exemplo, com 3 discos e pinos chamados "A", "B" e "C":

-Primeiro, 2 discos são movidos de "A" para "B" usando "C" como auxiliar.
-Depois, o disco maior é movido de "A" para "C".
-Por último, os 2 discos em "B" são movidos para "C" usando "A" como auxiliar.~

Esse processo continua se repetindo, quebrando o problema até que reste apenas um disco, que é movido diretamente. A recursão permite resolver o problema porque cada etapa é resolvida em termos de subproblemas menores, até atingir o caso base.

"""