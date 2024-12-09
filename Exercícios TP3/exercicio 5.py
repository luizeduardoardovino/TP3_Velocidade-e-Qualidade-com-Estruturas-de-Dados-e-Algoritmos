# 1) QuickSort:
# O QuickSort é um algoritmo de ordenação baseado na estratégia de divisão e conquista.
# Ele escolhe um elemento como pivô, particiona o array em duas partes com base nesse pivô,
# e depois ordena recursivamente as duas partes. Abaixo está a implementação:

def quicksort(arr):
    if len(arr) <= 1:
        return arr  

    
    pivot = arr[-1]

    
   
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    
    return quicksort(left) + [pivot] + quicksort(right)

# - A estratégia de divisão e conquista do QuickSort funciona da seguinte forma:
#   - Divisão: o array é dividido em duas partes com base no pivô.
#   - Conquista: cada parte é ordenada recursivamente usando a mesma lógica.
#   - Combinação: os resultados das partes ordenadas são concatenados.
# - O caso base é quando o array tem tamanho 0 ou 1, pois ele já está ordenado.

# Complexidade de tempo:
# - Melhor caso e caso médio: O(n log n), quando o pivô divide o array em partes aproximadamente iguais.
# - Pior caso: O(n^2), quando o pivô é sempre o menor ou o maior elemento, gerando divisões desbalanceadas.

# Complexidade de espaço:
# - Em média: O(log n), devido à profundidade da recursão.
# - No pior caso: O(n), para o espaço da pilha de chamadas quando o particionamento é desbalanceado.

# Exemplo de uso:
array = [10, 7, 8, 9, 1, 5]
print("Array original:", array)
print("Array ordenado:", quicksort(array))
