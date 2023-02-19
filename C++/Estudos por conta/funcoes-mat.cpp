#include <iostream>
#include <cmath>

int main(){

    double a = 10.5;
    double b = 20;
    double c;

    c = std::min(a, b); //minimo entre a e b
    std::cout << "c = " << c << std::endl;

    c = std::max(a, b); //maximo entre a e b
    std::cout << "c = " << c << std::endl;

    c = pow(2, 3); //2 elevado a 3
    std::cout << "c = " << c << std::endl;

    c = sqrt(25); //raiz quadrada de 25
    std::cout << "c = " << c << std::endl;

    c = abs(-10); //valor absoluto de -10
    std::cout << "c = " << c << std::endl;

    c = round(a); //arredonda 10.5 para o valor absoluto mais proximo
    std::cout << "c = " << c << std::endl;

    c = ceil(a); //arredonda 10.5 para o valor absoluto acima
    std::cout << "c = " << c << std::endl;

    c = floor(a); //arredonda 10.5 para o valor absoluto abaixo
    std::cout << "c = " << c << std::endl;

    return 0;
}