#include <iostream>

/* switch-case é uma estrutura de controle de fluxo de execução que permite que o programa execute um bloco de código dependendo do valor de uma variável.
É muito usado para substituir o uso de if-else quando se tem muitas condições.
*/

int main(){
    int month;
    std::cout << "Digite o número do mês: ";
    std::cin >> month;

    /*
    if(month == 1){
        std::cout << "Janeiro" << std::endl;
    }
    else if(month == 2){
        std::cout << "Fevereiro" << std::endl;
    }
    else if(month == 3){
        std::cout << "Março" << std::endl;
    }
    */

    // Da forma demonstrada acima, o processo iria ficar com muitas linhas de código, o que torna o código mais difícil de ler e manter.
    // Para resolver isso, podemos usar o switch-case:

    switch(month){  // "Switch" recebe uma função a ser avaliada, e "case" recebe os valores que serão comparados com a função.
        case 1:
            std::cout << "Janeiro" << std::endl;
            break;
        case 2:
            std::cout << "Fevereiro" << std::endl;
            break;
        case 3:
            std::cout << "Março" << std::endl;
            break;
        case 4:
            std::cout << "Abril" << std::endl;
            break;
        case 5:
            std::cout << "Maio" << std::endl;
            break;
        case 6:
            std::cout << "Junho" << std::endl;
            break;
        case 7:
            std::cout << "Julho" << std::endl;
            break;
        case 8:
            std::cout << "Agosto" << std::endl;
            break;
        case 9:
            std::cout << "Setembro" << std::endl;
            break;
        case 10:
            std::cout << "Outubro" << std::endl;
            break;
        case 11:
            std::cout << "Novembro" << std::endl;
            break;
        case 12:
            std::cout << "Dezembro" << std::endl;
            break;
        default:
            std::cout << "Mês inválido" << std::endl;
            break;
    }

    char grade;
    std::cout << "Digite a nota: ";
    std::cin >> grade;

    switch(grade){
    case 'A':
        std::cout << "Excelente" << std::endl;
        break;
    case 'B':
        std::cout << "Muito bom" << std::endl;
        break;
    case 'C':
        std::cout << "Bom" << std::endl;
        break;
    case 'D':
        std::cout << "Razoável" << std::endl;
        break;
    case 'F':
        std::cout << "Insuficiente" << std::endl;
        break;

    default:
        break;
    }

    return 0;
}