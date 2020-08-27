# CalculatingDistances
Calcula distância euclidiana e distancia de manhattan de uma base de dados.

Para executar o código é necessário informar os argumentos de acordo com a lista abaixo:
 - -inputFile - arquivo que será processado. É importante que ele não tenha espaços no nome, pois o código entenderá como um novo argumento e dará erro. Além disso, o arquivo deve conter apenas valores decimais
 - -sep - identificador de nova coluna
 - -dec - identificador de casa decimal
 - -distance - codigo da distancia a ser calculada. 1 para distancia euclidiana e 2 para distancia de manhattan
 - -outputFile - arquivo de saída


Exemplo de chamada do código no prompt:

```sh
$ python main.py -inputFile input.csv -sep , -dec . -distance 1 -outputFile distances.csv
```

É necessário que tenha as bibliotecas pandas e argparse instaladas no ambiente, caso não tenha, instalar utilizando os seguintes comandos no prompt:

```sh
$ pip install argparse
$ pip install pandas
```
