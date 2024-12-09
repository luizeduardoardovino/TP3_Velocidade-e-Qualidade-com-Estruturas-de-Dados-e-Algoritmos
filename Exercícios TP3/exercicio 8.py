# Problemas Comuns em Algoritmos Recursivos:
# - Limites de profundidade de chamada:
#   - A maioria das linguagens impõe um limite no número de chamadas recursivas que podem ser feitas.
#   - Se esse limite for excedido (em problemas com muitas divisões ou grandes entradas), ocorre um erro de "stack overflow".
#
# - Repetição excessiva de cálculos:
#   - Alguns algoritmos recursivos, como o Fibonacci, recalculam os mesmos subproblemas várias vezes.
#   - Isso aumenta exponencialmente o tempo de execução, afetando o desempenho.
#
# - Quando a recursão pode não ser recomendada:
#   - Problemas que requerem grande profundidade de chamada sem otimizações, como memoization.
#   - Problemas com espaço limitado na pilha de chamadas ou que podem ser resolvidos iterativamente com a mesma eficiência.

# Exemplo de Otimização: Usando Memoization
# Memoization armazena os resultados de subproblemas já calculados, evitando recalculá-los.
# Abaixo está um exemplo otimizado para o cálculo de Fibonacci:

def fibonacci_memo(n, memo={}):
    """
    Calcula o n-ésimo número de Fibonacci usando memoization.

    Args:
        n (int): O índice do número de Fibonacci.
        memo (dict): Um dicionário para armazenar resultados de subproblemas.

    Returns:
        int: O n-ésimo número de Fibonacci.
    """
    if n in memo:  # Verifica se o resultado já foi calculado.
        return memo[n]
    if n <= 1:  # Caso base: Fibonacci(0) = 0, Fibonacci(1) = 1.
        return n
    # Calcula e armazena o resultado no dicionário.
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# - A memoization evita a repetição excessiva de cálculos, melhorando o desempenho.
# - Complexidade de tempo: O(n), pois cada subproblema é calculado apenas uma vez.
# - Complexidade de espaço: O(n), devido ao armazenamento dos resultados na memória.

# Exemplo de uso:
n = 10
print(f"O {n}-ésimo número de Fibonacci é: {fibonacci_memo(n)}")

# 3) Alternativa: Conversão para Iterativo
# Outra forma de otimizar funções recursivas é convertê-las em versões iterativas,
# reduzindo o uso da pilha de chamadas. Abaixo está o Fibonacci em forma iterativa:

def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# - Essa abordagem usa apenas O(1) de espaço adicional.
# - É preferida quando o problema pode ser resolvido sem a necessidade de recursão.

# Conclusão:
# - A recursão é poderosa, mas pode ser limitada por problemas de profundidade de chamada e repetição de cálculos.
# - Usar memoization ou converter para uma abordagem iterativa pode contornar esses desafios,
#   tornando os algoritmos mais eficientes e escaláveis.
