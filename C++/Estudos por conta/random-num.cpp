#include <iostream>
// #include <cstdlib>
// #include <ctime>

/*A função rand retorna um numero aleatório, dessa forma, para determinar o alcance desses numeros, é necessária a seguinte sintaxe:
    rand() % (max - min + 1) + min
    onde max é o maior numero que se deseja e min é o menor numero que se deseja.
    O +1 é necessário para que o numero maximo seja incluido no alcance.
    O +min é necessário para que o numero minimo seja incluido no alcance.
    O resultado dessa expressão é um numero inteiro.
    Para gerar numeros reais, é necessário usar a função rand() / (RAND_MAX + 1.0), onde RAND_MAX é uma constante definida na biblioteca cstdlib.
    O resultado dessa expressão é um numero real.
    Para gerar numeros aleatórios com semente, é necessário usar a função srand(time(NULL)), onde time(NULL) retorna o tempo atual em segundos.
    O resultado dessa expressão é um numero inteiro.
*/

int main(){

    srand(time(NULL));
    int numero = (rand() % 100 + 1);

    std::cout << numero << std::endl;

    return 0;    
}