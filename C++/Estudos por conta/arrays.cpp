#include <iostream>

/* As arrays são formas de armazenar mais de um dado dentro de uma mesma variável.
Dessa forma, uma array pode ser declarada da seguinte forma:
tipo nome[] = {valor1, valor2, valor3, ...};
*/

int main(){

    std::string carros[] = {"BMW", "Ferrari", "Lamborghini", "Porsche"};
    std::string modelos[4];

    modelos[0] = "X5";
    modelos[1] = "F40";
    modelos[2] = "Aventador";
    modelos[3] = "911";

    std::cout << carros[0] << std::endl;
    std::cout << carros[1] << std::endl;
    std::cout << carros[2] << std::endl;
    std::cout << carros[3] << std::endl;

    return 0;
}