#include <iostream>

/* O escopo de uma variável é a região do programa em que a variável é visível. 
    Uma variável é visível a partir do ponto em que ela é declarada até o final do escopo em que ela foi declarada.
    O escopo de uma variável pode ser local ou global.
    Uma variável local é declarada dentro de uma função. Ela só pode ser usada dentro dessa função.
    Uma variável global é declarada fora de uma função. Ela pode ser usada em qualquer lugar do programa.
*/

void print();

int x = 2; // variável global

int main(){

    int x = 1; // variável local
    print();
    return 0;
}

void print(){
    std::cout << x << std::endl; // irá imprimir o valor da variável global, que no caso é 2, pois a variável local foi declarada dentro da função main, e não da função print.
    
}