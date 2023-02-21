#include <iostream>

/* Em C++, pode-se ter mais de uma função com o mesmo nome, desde que elas tenham parâmetros diferentes. Isso é chamado de sobrecarga de função. 
    A sobrecarga de função é usada para criar funções que fazem a mesma coisa, mas com parâmetros diferentes.
    Assim, criando artificialmente alguns parametros opcionais, como no exemplo abaixo.
*/

void fazerpizza();
void fazerpizza(std::string sabor);
void fazerpizza(std::string sabor, std::string sabor2);
void fazerpizza(std::string sabor, std::string sabor2, std::string sabor3);

int main(){

    fazerpizza("peperoni", "tomate");

    return 0;
}

void fazerpizza(){
    std::cout << "aqui está sua pizza!" << std::endl;
}

void fazerpizza(std::string sabor){
    std::cout << "aqui está sua pizza de " << sabor << std::endl;
}

void fazerpizza(std::string sabor, std::string sabor2){
    std::cout << "aqui está sua pizza de " << sabor << " com " << sabor2 << std::endl;
}

void fazerpizza(std::string sabor, std::string sabor2, std::string sabor3){
    std::cout << "aqui está sua pizza de " << sabor << " com " << sabor2 << " e " << sabor3 << std::endl;
}