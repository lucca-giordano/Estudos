#include <iostream>

int main(){

    //fazendo conversão de tipos

    int questoes = (double) 10;

    int acertos = 8;
    double percentual = (double)acertos / questoes * 100;

    std::cout << "percentual = " << percentual << "%" << std::endl;

    //sem conversão de tipos

    int questoes2 = 10;
    int acertos2 = 8;
    double percentual2 = acertos2 / questoes2 * 100;
    std::cout << "percentual2 = " << percentual2 << "%" << std::endl;

    return 0;
}