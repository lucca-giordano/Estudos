#include <iostream>
#include <cmath>

int main(){
    double a, b, c;
    std::cout << "Digite o valor de a: ";
    std::cin >> a;
    std::cout << "Digite o valor de b: ";
    std::cin >> b;
    c = sqrt(pow(a, 2) + pow(b, 2));
    std::cout << "O valor de c é: " << c << std::endl;
    return 0;
}