#include <iostream>

int main(){
    std::string name;
    std::cout << "Digite seu nome: ";
    std::getline(std::cin, name);

    if(name.empty()){
        std::cout << "Nome vazio" << std::endl;
    } else {
        std::cout << "Nome: " << name << std::endl;
    }

    //name.length() retorna o tamanho da string
    //name.empty() retorna true se a string estiver vazia
    //name.clear() limpa a string
    //name.append("texto") adiciona texto ao final da string
    //name.insert(0, "texto") insere texto na posição 0
    //name.erase(0, 3) apaga 3 caracteres a partir da posição 0
    //name.find("texto") retorna a posição do texto
    //name.substr(0, 3) retorna uma substring a partir da posição 0 com 3 caracteres
    //name.replace(0, 3, "texto") substitui 3 caracteres a partir da posição 0 por "texto"

    return 0;
}