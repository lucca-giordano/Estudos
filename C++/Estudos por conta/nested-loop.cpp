#include <iostream>

/* "Nested loops" é basicamente quando se usa um loop dentro de outro. 
    O loop interno é executado completamente para cada iteração do loop externo.
    No caso do loop for, é necessário uma variável para se manter a contagem, e essa variável deve ser diferente para cada loop.
    Então, convencionalmente usa-se a letra i para o loop externo e a letra j para o loop interno.
*/

int main(){

    int linhas;
    int colunas;
    char simbolo;

    std::cout << "Digite o número de linhas: ";
    std::cin >> linhas;
    std::cout << "Digite o número de colunas: ";
    std::cin >> colunas;
    std::cout << "Digite o símbolo: ";
    std::cin >> simbolo;

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            std::cout << simbolo;
        }
        std::cout << std::endl;
    }

    return 0;
}