#include <iostream>

/* As arrays são formas de armazenar mais de um dado dentro de uma mesma variável.
Dessa forma, uma array pode ser declarada da seguinte forma:
tipo nome[] = {valor1, valor2, valor3, ...};
*/

int main(){

    std::string carros[] = {"BMW", "Volvo", "Ford"};
    std::cout << carros[0] << std::endl; // irá imprimir o valor da array na posição 0, que no caso é BMW.
    std::cout << carros[1] << std::endl; // irá imprimir o valor da array na posição 1, que no caso é Volvo.
    std::cout << carros[2] << std::endl; // irá imprimir o valor da array na posição 2, que no caso é Ford.

    std::string carro_modelos [] = {{"BMW", "Volvo", "Ford"}, {"X5", "XC90", "Fiesta"}}; // array bidimensional
    std::cout << carro_modelos[0][0] << std::endl; // irá imprimir o valor da array na posição 0, que no caso é BMW.
    std::cout << carro_modelos[0][1] << std::endl; // irá imprimir o valor da array na posição 1, que no caso é Volvo.
    std::cout << carro_modelos[0][2] << std::endl; // irá imprimir o valor da array na posição 2, que no caso é Ford.
    std::cout << carro_modelos[1][0] << std::endl; // irá imprimir o valor da array na posição 0, que no caso é X5.
    std::cout << carro_modelos[1][1] << std::endl; // irá imprimir o valor da array na posição 1, que no caso é XC90.
    std::cout << carro_modelos[1][2] << std::endl; // irá imprimir o valor da array na posição 2, que no caso é Fiesta.


    return 0;
}