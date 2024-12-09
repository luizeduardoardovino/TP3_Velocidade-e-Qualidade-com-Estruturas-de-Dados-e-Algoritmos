# 1) Complexidade de Tempo:
# - Melhor caso: O(n log n)
#   - Quando o pivô escolhido divide o array em duas partes aproximadamente iguais.
#   - Cada divisão gera log n níveis de recursão, e em cada nível, são realizadas n comparações.
#   - Assim, o tempo total é proporcional a n * log n.
#
# - Caso médio: O(n log n)
#   - Estatisticamente, a escolha do pivô divide o array de forma balanceada na maioria dos casos.
#   - O comportamento médio segue a mesma análise do melhor caso, resultando em n * log n operações.
#
# - Pior caso: O(n^2)
#   - Ocorre quando o pivô escolhido é sempre o menor ou o maior elemento, gerando divisões desbalanceadas.
#   - Isso cria uma árvore de recursão de altura n, onde cada nível realiza n comparações.
#   - Nesse caso, o tempo total é proporcional a n^2.

# 2) Complexidade de Espaço:
# - Em média: O(log n)
#   - A profundidade da pilha de chamadas é log n, porque o array é dividido de forma balanceada.
#
# - No pior caso: O(n)
#   - Ocorre quando o particionamento é desbalanceado, resultando em uma árvore de recursão com altura n.

# Conclusão:
# - O QuickSort é eficiente no caso médio e no melhor caso, com complexidade de tempo O(n log n).
# - No entanto, no pior caso, ele pode ter um desempenho ruim, com complexidade O(n^2).
# - O uso de estratégias para escolher pivôs melhores (como o pivô mediano ou aleatório) pode ajudar a evitar o pior caso.
