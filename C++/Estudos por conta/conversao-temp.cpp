#include <iostream>

int main(){
    double temp;
    char escala;

    std::cout << "Digite a temperatura: ";
    std::cin >> temp;
    std::cout << "Digite a escala (C/F): ";
    std::cin >> escala;

    switch (escala){
    case 'C':
        std::cout << "Temperatura em Fahrenheit: " << (temp * 9/5) + 32 << std::endl;
        break;
    case 'F':
        std::cout << "Temperatura em Celsius: " << (temp - 32) * 5/9 << std::endl;
        break;
    default:
        std::cout << "Escala inválida" << std::endl;
        break;
    }

    return 0;
}