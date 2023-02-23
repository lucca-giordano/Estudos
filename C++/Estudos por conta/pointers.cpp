#include <iostream>

using namespace std;

int main(){
    // This code creates a variable called name and assigns the value "Joao" to it
    string name = "Joao"; 

    // This code creates a pointer called pName and assigns the address of the variable name to it
    string *pName = &name;

    cout << "Name: " << name << endl;
    cout << "Name address: " << &name << endl;
    
    cout << "Pointer name: " << pName << endl;
    cout << "Pointer name value: " << *pName << endl;

    return 0;
}