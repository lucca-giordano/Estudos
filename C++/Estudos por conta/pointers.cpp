#include <iostream>

using namespace std;

int main(){

    string carros[3] = {"Ferrari", "Lamborghini", "Porsche"};
    string *pCarros = carros;
    string *pUltimoCarro = &carros[2];

    cout << "Carros: " << carros << endl;
    cout << "pCarros: " << pCarros << endl;
    cout << "pCarros value: " << *pCarros << endl;
    cout << "pUltimoCarro: " << pUltimoCarro << endl;
    cout << "pUltimoCarro value: " << *pUltimoCarro << endl;

    return 0;
}