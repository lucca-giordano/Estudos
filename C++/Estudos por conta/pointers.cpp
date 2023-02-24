#include <iostream>

using namespace std;

int main(){

    string carros[3] = {"Ferrari", "Lamborghini", "Porsche"};
    string *pCarros = carros;

    cout << "Carros: " << carros << endl;
    cout << "pCarros: " << pCarros << endl;

    return 0;
}