#include <iostream>

int main(){
    const double PI =3.14159;
    double radius = 10;
    double circumference = 2 * PI * radius;

    const int LIGHT_SPEED = 299792458;
    const int WIDTH = 1920;
    const int HEIGHT = 1080;
    int area = WIDTH * HEIGHT;

    std::cout << "circumference = " << circumference << "cm" << std::endl;
    std::cout << "area = " << area << "px" << std::endl;
}