#include <iostream>

namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main(){
    
    using namespace first;

    int x = 3;

    std::cout << "x = " << x << std::endl;
    std::cout << "first::x = " << first::x << std::endl;
    std::cout << "second::x = " << second::x << std::endl;

    return 0;
}

/*
A função dos namespaces é para evitar conflitos entre nomes de variaveis
*/