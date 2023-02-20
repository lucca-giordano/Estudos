#include <iostream>

//Operadores lógicos são usados para comparar valores booleanos (true ou false).
//Existem três operadores lógicos: && (e), || (ou) e ! (não).

int main(){

    int temp;
    std::cout << "Digite a temperatura: ";
    std::cin >> temp;

    if (temp > 0 && temp < 30){
        std::cout << "Está normal" << std::endl;
    }
    else if (temp <= 0 || temp >= 30){
        std::cout << "Está estranho" << std::endl;
    }

    return 0;
}