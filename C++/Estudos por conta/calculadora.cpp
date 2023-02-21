#include <iostream>

int main(){
    double num1, num2, result;
    char op;

    std::cout << "Digite o primeiro número: ";
    std::cin >> num1;
    std::cout << "Digite o segundo número: ";
    std::cin >> num2;
    std::cout << "Digite a operação (+ - * /): ";
    std::cin >> op;

    switch (op){
    case '+':
        result = num1 + num2;
        std::cout << "Resultado: " << result << std::endl;
        break;
    case '-':
        result = num1 - num2;
        std::cout << "Resultado: " << result << std::endl;
        break;
    case '*':
        result = num1 * num2;
        std::cout << "Resultado: " << result << std::endl;
        break;
    case '/':
        result = num1 / num2;
        std::cout << "Resultado: " << result << std::endl;
        break;
    
    default:
        std::cout << "Operação inválida" << std::endl;
        break;
    }

    return 0;
}