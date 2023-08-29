# esse programa é um teste para eu poder gerar números aleatórios
# sem o uso da biblioteca random

# importando biblioteca de tempo para eu poder pegar os segundos
from datetime import datetime as date


# criando a função para gerar o número aleatório 
def gerar_aleatorio(intervalor_min, intervalor_max):
    """
    Essa função é um estudo meu para entender a geração de números aleatórios

    Ela recebe como parametro 2 elementos, o menor e o maior valor do intervalor.
    Ela retornará um número entre esse intervalo
    """

    tempo = date.now()
    segundo = tempo.second

    # criando o gerador 
    num_grande = 17462267  # numero grande escolhido para aumentar aleatoriedade

    tamanho = intervalor_max - intervalor_min  # determinando o tamanho do intervalo

    gerador = segundo * num_grande 
    # aproveito que o segundo muda toda hora para aumentar aleatoriedade do programa

    num_gerado = (gerador % tamanho) + intervalor_min

    # o uso do % é para poder pegar sempre no intervalo
    # tipo: resto da divisão de 123 por 10 (com intervalo max de 10 e min 0) é 12 e sobra 3
    # esse 3 tá no limite desejado
    # ao somar o intervalor_min eu posso, dependendo, gerar um número negativo
    # ex: a divisão resulta em 4 e o intervalo_min é -5: 4 + (-5) é -1  :D

    return num_gerado


# função usada para tratar entrada de números
def tratar_num():
    """
    Função usada para tratar a entrada de números

    Se não escrever um inteiro o loop será ativo.
    Se escrever um inteiro, retornará ele.
    """
    while True:
        try:
            return int(input(': ').strip())  # só sai do loop quando digitar um número

        except ValueError:
            print('escreva um número apenas')  # se não digitar um número avisa o erro e entra no loop de novo



# código principal
print('escolha o intervalo para a geração do número')

print('menor valor para ele')
escolha_min = tratar_num()

print('maior valor para ele')
escolha_max = tratar_num()


resultado = gerar_aleatorio(escolha_min ,escolha_max)

print(resultado)
