# 1) QuickSelect:
# O QuickSelect é um algoritmo baseado na estratégia de divisão e conquista, semelhante ao QuickSort.
# Ele é usado para encontrar o k-ésimo menor elemento em um array sem a necessidade de ordenar toda a lista.
# Abaixo está a implementação:

def quickselect(arr, k):
    """
    Encontra o k-ésimo menor elemento em uma lista usando o algoritmo QuickSelect.

    Args:
        arr (list): Lista de elementos.
        k (int): Índice (1-based) do k-ésimo menor elemento.

    Retornos:
        int: O k-ésimo menor elemento da lista.
    """
    if len(arr) == 1:  # Caso base: apenas um elemento na lista.
        return arr[0]

    # Escolha do pivô (neste caso, o último elemento do array).
    pivot = arr[-1]

    # Particionamento: separar elementos menores ou iguais e maiores que o pivô.
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Tamanho do lado esquerdo (número de elementos menores ou iguais ao pivô).
    left_size = len(left) + 1

    if k == left_size:  # O pivô é o k-ésimo menor elemento.
        return pivot
    elif k < left_size:  # O k-ésimo menor está no lado esquerdo.
        return quickselect(left, k)
    else:  # O k-ésimo menor está no lado direito.
        return quickselect(right, k - left_size)

# - O algoritmo QuickSelect funciona dividindo o problema em partes menores:
#   - Escolhe um pivô e particiona o array.
#   - Decide recursivamente em qual lado (esquerdo ou direito) está o k-ésimo menor elemento.
#   - Isso reduz o tamanho do problema a cada chamada recursiva, tornando o algoritmo eficiente.
#
# Exemplo de uso:
array = [10, 4, 5, 8, 6, 11, 26]
k = 4
print(f"O {k}-ésimo menor elemento é: {quickselect(array, k)}")

# Comparação de desempenho com busca linear:
# 1) QuickSelect:
# - Melhor caso: O(n), quando o particionamento é balanceado.
# - Caso médio: O(n), pois reduz o problema em partes menores de forma eficiente.
# - Pior caso: O(n^2), quando o particionamento é altamente desbalanceado (semelhante ao QuickSort).

# 2) Busca Linear:
# - Complexidade: O(n), pois percorre toda a lista uma vez para encontrar o k-ésimo menor elemento.

# Comparação:
# - No caso médio, o QuickSelect é mais eficiente porque evita percorrer toda a lista.
# - No entanto, a busca linear é mais simples e não depende de particionamento ou recursão.
# - QuickSelect é preferido quando o problema envolve listas grandes ou múltiplas consultas ao k-ésimo menor elemento.
