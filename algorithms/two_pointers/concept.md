## Two Pointers

O algortirmo **two pointers** tem como objetivo manipular dois ponteiros (ou índices, mais comumente), para performar manipulações em alguma estrutura de dados, sendo a mais comum os arrays.

Ela se encaixa em diversos tipos de operações, como inverter arrays e strings, auxiliar em buscas binárias e também quando se trabalha com outros padrão de algoritmo chamado de slidwing window.

As principais estratégias são:

- **Ponteiros convergentes**: Um ponteiro começa no inicio (index 0) e outro no fim (index len(array) - 1), movendo-se um em direção ao outro. Comum para encontrar palíndromos ou inverter arrays.

- **Ponteiros na mesma direção**: Dois ponteiros se movem na mesma direção, porém um diferente do outro, dada alguma condição específica. Muito comum em operações com sliding window,

- **Fast and Slow**: Um ponteiro move linearmente (slow), enquanto o outro se move o dobro, triplo, etc (fast). Muito útil em operações com linked-lists, para detectar o meio da lista ou ciclos.

## Complexidade

Normalmente, esse algoritmo terá complexidade temporal O(n), pois irá percorrer o array inteiro, no pior dos casos, e complexidade espacial de O(1), alocando apenas os dois ponteiros para performar a lógica.
