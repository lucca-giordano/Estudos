#include <iostream>

int main(){
    int x; //declaração
    x = 5; //atribuição

    int y = 6; //declaração e atribuição
    double z = 7.5; //declaração e atribuição

    double sum = x + z; //declaração, atribuição e operação

    char index = 'c'; //declaração e atribuição de um caractere

    bool isTrue = true; //declaração e atribuição de um booleano
    std::string name = "John"; //declaração e atribuição de uma string
    std::string lastname = ""; //declaração e atribuição de uma string

    std::cout << "index = " << index << std::endl; //imprime o valor de index
    std::cout << "isTrue = " << isTrue << std::endl; //imprime o valor de isTrue
    std::cout << "name = " << name << std::endl; //imprime o valor de name

    std::cout << "x = " << x << std::endl; //imprime o valor de x
    std::cout << "y = " << y << std::endl; //imprime o valor de y
    std::cout << "z = " << z << std::endl; //imprime o valor de z
    std::cout << "sum = " << sum << std::endl; //imprime o valor de sum
}