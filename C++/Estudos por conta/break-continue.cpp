#include <iostream>

/* O operador break é usado para sair de um loop. Ele pode ser usado em loops while, do-while e for.
    O operador continue é usado para pular uma iteração de um loop. Ele pode ser usado em loops while, do-while e for.
*/

int main(){

    for(int i = 0; i <= 20; i++){
        if(i == 13){
            continue;
        }
        std::cout << i << std::endl;
    }

        for(int i = 0; i <= 20; i++){
        if(i == 13){
            break;
        }
        std::cout << i << std::endl;
    }


    return 0;
}