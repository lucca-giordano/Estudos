#include <iostream>

/* No C++, os operadores matemáticos são:

+ para soma
- para subtração
* para multiplicação
/ para divisão
% para resto da divisão

Dessa forma pode-se elaborar qualquer função matemática com base nos conceitos mais básicos, 
sem contar com as funções ja existentes em cmath.h, que facilitam a crianção desse tipo de coisa.

 */

int main(){

    int students = 20;
    students = students + 1;
    students += 1;
    students++;

    std::cout << "students = " << students << std::endl;
    students = 20;

    students = students - 1;
    students -= 1;
    students--;

    std::cout << "students = " << students << std::endl;
    students = 20;

    students = students * 2;
    students *= 2;
    
    std::cout << "students = " << students << std::endl;
    students = 20;

    students = students / 2;
    students /= 2;

    std::cout << "students = " << students << std::endl;
    students = 20;
    
    students = students % 3;
    students %= 3;

    std::cout << "students = " << students << std::endl;
    students = 20;

    double number = 10;
    number /= 3;

    std::cout << "number = " << number << std::endl;

    return 0;
}