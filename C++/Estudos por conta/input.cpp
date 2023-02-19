#include <iostream>

// cout = console output
// cin = console input
// getline = pega a linha inteira
// ws = white space

int main(){
    std::string name;
    int age;

    std::cout << "Digite sua idade: ";
    std::cin >> age;

    std::cout << "Digite seu nome completo: ";
    std::getline(std::cin >> std::ws, name);

    std::cout << "Ola " << name << "!" << std::endl;
    std::cout << "Voce tem " << age << " anos." << std::endl;
}