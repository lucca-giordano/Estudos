# C++

Aqui estão todas as minhas anotações sobre C++, desde o mais básico até o mais complexo.

![C++](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png)

---

## Índice

- [Iniciando um projeto](#iniciando-um-projeto)
    - [Sintaxe](#sintaxe)
        - [#include](#include)
        - [int main()](#int-main)
        - [return 0;](#return-0)
    - [Hello World](#hello-world)
        - [std::cout](#stdcout)
        - [<< "Hello World!"](#-hello-world)
        - [std::endl](#stdendl)
- [Variáveis](#variáveis-e-tipos-de-dados)
    - [Tipos de Dados](#tipos-de-dados)
        - [Inteiros](#inteiros)
        - [Caracteres](#caracteres)
        - [Strings](#strings)
        - [Ponto Flutuante](#ponto-flutuante)
        - [Booleano](#booleano)
        - [Valor Nulo](#valor-nulo)
    - [Variáveis](#variáveis)
- [Constantes](#constantes)

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

# Variáveis e Tipos de Dados

As variáveis podem ser vistas como um espaço na memória do computador, que pode ser usado para armazenar valores. O C++ é uma linguagem de tipagem forte, o que significa que cada variável tem um tipo específico, e você não pode mudar o tipo de uma variável depois de criá-la.

## Tipos de Dados

O C++ possui 6 tipos de dados básicos:

- Inteiros
- Caracteres
- Strings
- Ponto Flutuante
- Booleano
- Valor Nulo

### Inteiros

Os tipos de dados inteiros são usados para armazenar valores inteiros (números sem casas decimais). O C++ suporta 4 tipos de dados inteiros:

- short int
- int
- long int
- long long int

### Caracteres

Os tipos de dados de caracteres são usados para armazenar caracteres. O C++ suporta 2 tipos de dados de caracteres:

- char
- wchar_t

### Strings

Os tipos de dados de string são usados para armazenar strings. O C++ suporta 2 tipos de dados de string:

- string
- wstring

### Ponto Flutuante

Os tipos de dados de ponto flutuante são usados para armazenar valores de ponto flutuante (números com casas decimais). O C++ suporta 3 tipos de dados de ponto flutuante:

- float
- double
- long double

### Booleano

Os tipos de dados booleanos são usados para armazenar valores booleanos (true ou false). O C++ suporta 1 tipo de dados booleano:

- bool

### Valor Nulo

Os tipos de dados de valor nulo são usados para armazenar um valor nulo. O C++ suporta 1 tipo de dados de valor nulo:

- nullptr

## Variáveis

As variáveis são usadas para armazenar valores. Para criar uma variável, você deve especificar o tipo de dados e o nome da variável.

```cpp

int x = 5; // x é um inteiro com o valor 5

char y = 'a'; // y é um caractere com o valor 'a'

std::string z = "Hello World!"; // z é uma string com o valor "Hello World!"

float a = 5.5; // a é um ponto flutuante com o valor 5.5

bool b = true; // b é um booleano com o valor true

nullptr c = nullptr; // c é um valor nulo

```

# Constantes

As constantes são usadas para armazenar valores que não podem ser alterados de nenhuma maneira. Para criar uma constante, você deve especificar que é uma constante, o tipo de dados e o nome da constante.

```cpp

const int x = 5; // x é uma constante inteira com o valor 5

const char y = 'a'; // y é uma constante caractere com o valor 'a'

```
