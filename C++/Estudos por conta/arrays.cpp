#include <iostream>

/* As arrays são formas de armazenar mais de um dado dentro de uma mesma variável.
Dessa forma, uma array pode ser declarada da seguinte forma:
tipo nome[] = {valor1, valor2, valor3, ...};
*/

int main(){
   std::string carros[][3] = {{"Detomasso", "Ferrari", "Lamborghini"},
                              {"Ford", "Chevrolet", "Dodge"},
                              {"Bugatti", "Koenigsegg", "Pagani"}};

    std::cout << carros[0][0] << ", ";
    std::cout << carros[0][1] << ", ";
    std::cout << carros[0][2] << std::endl;

    std::cout << carros[1][0] << ", ";
    std::cout << carros[1][1] << ", ";
    std::cout << carros[1][2] << std::endl;

    std::cout << carros[2][0] << ", ";
    std::cout << carros[2][1] << ", ";
    std::cout << carros[2][2] << std::endl;

    return 0;
}