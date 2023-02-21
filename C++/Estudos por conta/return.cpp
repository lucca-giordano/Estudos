#include <iostream>

/* O operador return, devolve o valor gerado por uma função, assim, atribuindo o mesmo a uma váriável ou a uma outra função.
*/

double vol(double altura, double largura, double comprimento);

int main(){

    double altura, largura, comprimento;
    std::cout << "Digite a altura: ";
    std::cin >> altura;

    std::cout << "Digite a largura: ";
    std::cin >> largura;

    std::cout << "Digite o comprimento: ";
    std::cin >> comprimento;

    std::cout << "A area é: " << vol(altura, largura, comprimento) << std::endl;

    return 0;
}

double vol(double altura, double largura, double comprimento){
    return altura * largura * comprimento;
}