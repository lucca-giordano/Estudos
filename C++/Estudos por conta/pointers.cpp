#include <iostream>

using namespace std;

int main(){
    string name = "Joao";
    string *pName = &name;

    cout << "Name: " << name << endl;
    cout << "Name address: " << &name << endl;

    cout << "Pointer name: " << pName << endl;
    cout << "Pointer name value: " << *pName << endl;

    return 0;
}