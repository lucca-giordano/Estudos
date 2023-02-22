# C++

Aqui estão todas as minhas anotações sobre C++, desde o mais básico até o mais complexo.

---

## Índice

- [Iniciando um projeto](#iniciando-um-projeto)

# Iniciando um projeto

Todo projeto em C++ tem **alguns requesitos** para que você possa programar corretamente.

Dessa forma, todo arquivo `.cpp` deve ter o seguinte código:

```cpp
#include <iostream>
int main(){

    return 0;
}
```

Assim ja nos levando para o segundo tópico, a sintaxe do C++.

## Sintaxe

Por ser considerada uma linguagem de nível médio, o C++ possui uma sintaxe bem simples, mas que pode ser confusa para quem está começando. Por isso, vou explicar cada parte do código acima.

### #include

O `#include` é uma diretiva de pré-processamento, que serve para incluir arquivos de cabeçalho. Nesse caso, estamos incluindo o arquivo `iostream`, que é o arquivo de cabeçalho padrão da biblioteca padrão do C++.

### int main()

A função `main()` é a função principal de um programa em C++. Ela é a primeira função a ser executada quando o programa é iniciado.

### return 0;

A função `main()` deve retornar um valor inteiro, que é o código de saída do programa. O código de saída é um valor inteiro que é retornado para o sistema operacional quando o programa é finalizado. O valor 0 significa que o programa foi executado com sucesso. Caso contrário, o valor retornado é diferente de 0.

## Hello World

Agora que já sabemos como iniciar um projeto em C++, vamos fazer o nosso primeiro programa, o famoso "Hello World".

```cpp

#include <iostream>
int main(){
    std::cout << "Hello World!" << std::endl;
    return 0;
}

```

Agora vamos entender o código acima.

### std::cout

O `std::cout` é um objeto de fluxo de saída padrão, que é usado para imprimir texto na tela. O `std` é o namespace padrão do C++, que é um espaço de nomes que contém um conjunto de nomes. O `::` é o operador de resolução de escopo, que é usado para acessar um membro de um namespace.

### << "Hello World!"

O `<<` é o operador de inserção, que é usado para inserir um valor em um objeto de fluxo. Nesse caso, estamos inserindo a string "Hello World!" no objeto de fluxo de saída padrão.

### std::endl

O `endl` é um manipulador de fluxo, que é usado para inserir um caractere de nova linha no objeto de fluxo de saída padrão.

