#include <iostream>

/* As arrays são formas de armazenar mais de um dado dentro de uma mesma variável.
Dessa forma, uma array pode ser declarada da seguinte forma:
tipo nome[] = {valor1, valor2, valor3, ...};
*/

int main() {
    std::string carros[3][3] = {{"Detomasso", "Ferrari", "Lamborghini"},
                                {"Ford", "Chevrolet", "Dodge"},
                                {"Bugatti", "Koenigsegg", "Pagani"}};

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << carros[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}