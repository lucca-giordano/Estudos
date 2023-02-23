#include <iostream>

int main(){

    std::string nome = "João";
    int idade = 20;
    bool vivo = true;

    std::cout << &nome << std::endl;
    std::cout << &idade << std::endl;
    std::cout << &vivo << std::endl;

    return 0;
}