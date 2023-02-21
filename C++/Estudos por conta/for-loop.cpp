#include <iostream>

/* O operador for é usado para executar um bloco de código um número determinado de vezes.
    O for é composto por três partes:
        1. Inicialização: é executada uma vez antes do início do loop
        2. Condição: é verificada no início de cada iteração do loop. Se for verdadeira, o loop continua. Se for falsa, o loop termina.
        3. Incremento: é executado no final de cada iteração do loop, antes da próxima verificação da condição.
*/

int main(){

    for(int i = 3; i > 0; i--){
        std::cout << i << std::endl;
    }
    std::cout << "feliz aniversário! :D" << std::endl;
}