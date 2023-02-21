#include <iostream>

/* O operador while é usado para executar um bloco de código enquanto uma condição for verdadeira.
    Pode-se executar o código infinitamente colocando uma condição sempre verdadeira, como 1==1 ou true.

    O operador do while é parecido com o while, mas ele executa o código pelo menos uma vez antes de verificar a condição.
*/

int main(){

    int num;

    do{
        std::cout << "Digite um número: ";
        std::cin >> num;
    }while(num < 0);

    std::cout << "Seu número é: " << num << std::endl;

    return 0;
}