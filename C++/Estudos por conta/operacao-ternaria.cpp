#include <iostream>

//Operações ternárias são uma forma de simplificar o uso de if-else.
//Sua sintaxe é a seguinte: (condição) ? (resultado se verdadeiro) : (resultado se falso)
//Exemplo:

int main(){
    int nota;
    std::cout << "Digite a nota: ";
    std::cin >> nota;

    nota >= 6 ? std::cout << "Aprovado" << std::endl : std::cout << "Reprovado" << std::endl;

    int num;
    std::cout << "Digite um número: ";
    std::cin >> num;

    num % 2 == 0 ? std::cout << "Par" << std::endl : std::cout << "Ímpar" << std::endl;

    bool fome = true;
    std::cout << (fome ? "Estou com fome" : "Não estou com fome") << std::endl;

     return 0;
}