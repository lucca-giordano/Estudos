#include <iostream>

/* if e else são estruturas de controle de fluxo de execução, que permitem
 * que o programa execute um bloco de código ou outro, dependendo de uma
 * condição. */

int main(){
    int idade;
    std::cout << "Digite a sua idade: ";
    std::cin >> idade;
    if (idade >= 100){
        std::cout << "Idade inválida!" << std::endl;
    }
    else if (idade <= 0){
        std::cout << "Idade inválida!" << std::endl;
    }
    else if (idade >= 18){
        std::cout << "Bem vindo ao site!!" << std::endl;
    }

    else{
        std::cout << "Você não tem idade suficiente para acessar o site!" << std::endl;
    }
}