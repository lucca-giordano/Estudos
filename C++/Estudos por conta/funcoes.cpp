#include <iostream>

void parabens(std::string nome);

int main(){

    std::string palavra;
    std::cout << "Digite seu nome: ";
    std::getline(std::cin, palavra);

    parabens(palavra);
    parabens(palavra);
    parabens(palavra);

    return 0;
}

void parabens(std::string nome){
    std::cout << "Parabéns!" << nome << "!! :D" << std::endl;
}