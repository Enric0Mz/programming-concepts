## Sliding Window

Sliding window é uma técnica de resolução de algoritmos, que normalmente é implementada em Arrays ou Strings, em que se utiliza uma janela de items para executar certa ação. Ela é muito comum em problemas que precisam resultar em uma substring, ou subarray baseado em alguma condição especídica, evitando usar recálculo, normalmente com brute force, para resolução do problema.

Os dois principais métodos em que a sliding window é utilizada:

- **Tamanho variável**
  Em problema de janela variável, normalmente é pedido para achar o maior ou menor subarray, dado alguma condição, como a maior substring sem caractéres repetidos ou o maior subarray em que a soma dos elementos é menor que 10.

- **Tamanho fixo**
  Em problemas de janela fixa, normalmente o problema pede para achar algum subarray de tamanho k, por exemplo, e retornar esse array, dada alguma condição, por exemplo, o mairo subarray de tamanho k que contenha a maior soma do array.

## Complexidade

O algoritmo de sliding window normalmente tem complexidade temporal O(n), pois mesmo expandindo e retraindo a janela, a direção é sempre para a direita. Quanto a sua complexidade espacial, pode variar bastante entre O(n) e O(1), dependendo do que cada problema pede, em específico.
