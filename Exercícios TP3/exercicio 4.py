# 1) Algoritmo Recursivo para Fibonacci:
# O cálculo do n-ésimo número de Fibonacci é feito somando os dois números anteriores na sequência.
# Abaixo está o código:

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# - Para calcular fibonacci(n), o algoritmo faz duas chamadas recursivas: fibonacci(n-1) e fibonacci(n-2).
# - Essas chamadas se ramificam, gerando várias operações repetitivas.
# - A estrutura de chamadas forma uma árvore de recursão com altura n, onde cada nível cria subproblemas adicionais.
# - O número total de chamadas recursivas cresce exponencialmente, aproximadamente 2^n.

# Complexidade de tempo: O(2^n), que é exponencial.
# Complexidade de espaço: O(n), pois a profundidade máxima da pilha de recursão é n.

# 2) Algoritmo Recursivo para Fatorial:
# O cálculo do fatorial de n (n!) é feito multiplicando n pelos valores menores até 1.
# Abaixo está o código:

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# - Para calcular o fatorial de n, o algoritmo faz exatamente n chamadas recursivas.
# - Cada chamada resolve um subproblema menor até chegar ao caso base (n == 1 ou n == 0).
# - Não há ramificação das chamadas, ou seja, cada nível de recursão gera apenas uma nova chamada.

# Complexidade de tempo: O(n), pois há n chamadas recursivas.
# Complexidade de espaço: O(n), pois a profundidade da pilha de recursão é n.
