#include <iostream>

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