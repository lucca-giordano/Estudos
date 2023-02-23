#include <iostream>

/* As arrays são formas de armazenar mais de um dado dentro de uma mesma variável.
Dessa forma, uma array pode ser declarada da seguinte forma:
tipo nome[] = {valor1, valor2, valor3, ...};
*/

int main(){

int main(){
    int array[] = {1, 2, 3, 4, 5};
    printArray(array);
    return 0;
}

void printArray(int array[]){
    for(int x : array){
        std::cout << x << std::endl;
    }
}
}