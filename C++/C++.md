# C++

Aqui estão todas as minhas anotações sobre C++, desde o mais básico até o mais complexo.

![C++](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png)

---

## Índice

- [Iniciando um projeto](#iniciando-um-projeto)
- [Variáveis](#variáveis-e-tipos-de-dados)
- [Constantes](#constantes)
- [Namespaces](#namespace)
- [Type alias](#type-alias)
- [Operadores Aritméticos](#operadores-aritméticos)
- [Input de Dados](#input-de-dados)
- [Operadores condicionais](#operadores-condicionais)
- [Loops](#loops)
- [Funções](#funções)
- [Arrays](#arrays)


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

# Namespace

Os namespaces são usados para organizar o código em grupos lógicos e para evitar conflitos de nomes que possam ocorrer. Os namespaces podem ser definidos com a palavra-chave `namespace`.

```cpp

namespace primeiro_namespace{
    int x = 5;
}

namespace segundo_namespace{
    int x = 10;
}

int main(){
    std::cout << primeiro_namespace::x << std::endl; // 5
    std::cout << segundo_namespace::x << std::endl; // 10
    return 0;
}

```

# Type Alias

O type alias é usado para dar um nome alternativo a um tipo de dados existente. O type alias é definido com a palavra-chave `using` ou com a palavra-chave `typedef`.

```cpp

using inteiro_t = int;
typedef std::string str_t;

int main(){
    inteiro x = 5;
    std::cout << x << std::endl; // 5
    return 0;
}

```

**Pode-se notar o uso do '`_t`' no final do type alias definido. Por convenção, quando um alias para um tipo de dado é definido, usa-se '`_t`' ao final, para demonstrar sua origem.**

# Operadores aritméticos

Os operadores aritméticos são usados para realizar operações aritméticas (adição, subtração, multiplicação, divisão, etc.) em variáveis ou constantes. O C++ suporta 6 operadores aritméticos:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Módulo (%)
- Incremento (++)

## Adição (+)

O operador de adição é usado para adicionar dois valores.

```cpp

int x = 5;
int y = 10;
int z = x + y; // z = 15

```

## Subtração (-)

O operador de subtração é usado para subtrair dois valores.

```cpp

int x = 5;
int y = 10;
int z = x - y; // z = -5

```

## Multiplicação (*)

O operador de multiplicação é usado para multiplicar dois valores.

```cpp

int x = 5;
int y = 10;
int z = x * y; // z = 50

```

## Divisão (/)

O operador de divisão é usado para dividir dois valores.

```cpp

int x = 10
int y = 5;
int z = x / y; // z = 2

```

## Módulo (%)

O operador de módulo é usado para obter o resto da divisão de dois valores.

```cpp

int x = 10;
int y = 3;
int z = x % y; // z = 1

```

## Incremento (++)

O operador de incremento é usado para incrementar um valor em 1.

```cpp

int x = 5;
x++; // x = 6

```

# Funções matemáticas (cmath)

As funções matemáticas são usadas para realizar operações matemáticas (raiz quadrada, exponenciação, etc.). O C++ possui uma biblioteca padrão chamada cmath, que contém funções matemáticas. Algumas delas são:

- `sqrt(x)` - Retorna a raiz quadrada de x
- `pow(x, y)` - Retorna x elevado a y
- `abs(x)` - Retorna o valor absoluto de x
- `ceil(x)` - Retorna o menor inteiro maior ou igual a x
- `floor(x)` - Retorna o maior inteiro menor ou igual a x
- `round(x)` - Retorna o valor de x arredondado para o inteiro mais próximo
- `max(x, y)` - Retorna o maior valor entre x e y
- `min(x, y)` - Retorna o menor valor entre x e y

Claro, estas não são todas as funções matemáticas que o C++ possui, mas são as mais comuns. Além disso, você pode criar suas próprias funções matemáticas.

```cpp

#include <iostream>
#include <cmath>

int main(){
    std::cout << sqrt(25) << std::endl; // 5
    std::cout << pow(2, 3) << std::endl; // 8
    std::cout << abs(-5) << std::endl; // 5
    std::cout << ceil(5.5) << std::endl; // 6
    std::cout << floor(5.5) << std::endl; // 5
    std::cout << round(5.5) << std::endl; // 6
    std::cout << max(5, 10) << std::endl; // 10
    std::cout << min(5, 10) << std::endl; // 5
    return 0;
}

```

# Input de dados

O input de dados é usado para receber dados do usuário. Para receber dados do usuário, você deve usar a função `std::cin`.

Porém, esta função tem algumas limitações, como por exemplo, ela não consegue receber espaços em branco. Para contornar este problema, você deve usar a função `std::getline`.

Lembrando que, caso no seu código você use a função `std::getline` depois de usar a função `std::cin`, você deve usar a função `std::ws` para limpar o buffer de entrada.

```cpp

#include <iostream>

int main(){
    int x;
    std::cin >> x;
    std::cout << x << std::endl;

    std::string y;
    std::getline(std::cin >> std::ws, y);
    std::cout << y << std::endl;
    return 0;
}

```

# Operadores condicionais

## if, else if e else

O if, else if e else são usados para executar um bloco de código caso uma condição seja verdadeira. O if, else if e else são definidos com as palavras-chave `if`, `else if` e `else`.

```cpp

int x = 5;
if(x == 5){
    std::cout << "x é igual a 5" << std::endl;
}else if(x == 10){
    std::cout << "x é igual a 10" << std::endl;
}else{
    std::cout << "x não é igual a 5 nem a 10" << std::endl;
}

```

## switch

O switch é usado para executar um bloco de código caso uma condição seja verdadeira. O switch é definido com a palavra-chave `switch`.

```cpp

int x = 5;

switch(x){
    case 5:
        std::cout << "x é igual a 5" << std::endl;
        break;
    case 10:
        std::cout << "x é igual a 10" << std::endl;
        break;
    default:
        std::cout << "x não é igual a 5 nem a 10" << std::endl;
        break;
}

```

## Operação ternária

A operação ternária é usada para executar um bloco de código caso uma condição seja verdadeira. A operação ternária é definida com a sintaxe `condição ? caso_verdade : caso_falso`.

```cpp

int x = 5;

std::cout << (x == 5 ? "x é igual a 5" : "x não é igual a 5") << std::endl;

```

## Operadores de comparação

Os operadores de comparação são usados para comparar dois valores. Os operadores de comparação são:

- `==` - Igual
- `!=` - Diferente
- `>` - Maior que
- `>=` - Maior ou igual a
- `<` - Menor que
- `<=` - Menor ou igual a

## Operadores lógicos

Os operadores lógicos são usados para combinar duas ou mais condições. Os operadores lógicos são:

- `&&` - E
- `||` - Ou
- `!` - Não

Aqui estão alguns exemplos de operadores lógicos e de comparação:

```cpp

int x = 5;

if(x > 0 && x < 10){
    std::cout << "x é maior que 0 e menor que 10" << std::endl;
}

if(x == 5 || x == 10){
    std::cout << "x é igual a 5 ou a 10" << std::endl;
}

if(!(x == 5)){
    std::cout << "x não é igual a 5" << std::endl;
}

```

# Loops

## while

O while é usado para executar um bloco de código enquanto uma condição for verdadeira. O while é definido com a palavra-chave `while`.

```cpp

int x = 0;

while(x < 10){
    std::cout << x << std::endl;
    x++;
}

```

## do while

O do while é usado para executar um bloco de código enquanto uma condição for verdadeira, a diferença principal é que a ação é executada no mínimo uma vez antes de verificar a condição. O do while é definido com a palavra-chave `do`.

```cpp

int x = 0;

do{
    std::cout << x << std::endl;
    x++;
}while(x < 10);

```

## for

O for é usado para executar um bloco de código uma determinada quantidade de vezes. O for é definido com a palavra-chave `for`.

```cpp

for(int x = 0; x < 10; x++){
    std::cout << x << std::endl;
}

```

Os três exemplos de loops acima irão imprimir os números de 0 a 9.

## break

O break é usado para parar um loop. O break é definido com a palavra-chave `break`.

```cpp

for(int x = 0; x < 10; x++){
    if(x == 5){
        break;
    }
    std::cout << x << std::endl;
}

```

## continue

O continue é usado para pular uma iteração de um loop. O continue é definido com a palavra-chave `continue`.

```cpp

for(int x = 0; x < 10; x++){
    if(x == 5){
        continue;
    }
    std::cout << x << std::endl;
}

```

## Nested loops

Nested loops são loops dentro de loops. Nested loops são usados para executar um bloco de código uma determinada quantidade de vezes, mas com uma condição diferente.

```cpp

for(int x = 0; x < 10; x++){
    for(int y = 0; y < 10; y++){
        std::cout << x << " " << y << std::endl;
    }
}

```

## goto

goto é usado para pular para um ponto do código. goto é definido com a palavra-chave `goto`.

```cpp

int x = 0;

loop:
    std::cout << x << std::endl;
    x++;
    if(x < 10){
        goto loop;
    }

```

# Funções

## Definindo uma função

Uma função é um bloco de código que pode ser executado várias vezes. Uma função é definida com a palavra-chave `void` ou com um tipo de retorno e seu nome.

```cpp

void printHelloWorld(){
    std::cout << "Hello World" << std::endl;
}

```

É importante lembrar que, seu código é lido de cima para baixo, e c++ executa tudo que está dentro da função main. Ou seja, normalmente, as funções são definidas abaixo da função main, e logo acima da mesma é declarada, dessa forma:

```cpp

include <iostream>

void printHelloWorld();

int main(){
    printHelloWorld();
    return 0;
}

void printHelloWorld(){
    std::cout << "Hello World" << std::endl;
}

```

## Chamando uma função

Uma função é chamada com seu nome e parênteses.

```cpp

void printHelloWorld(){
    std::cout << "Hello World" << std::endl;
}

int main(){
    printHelloWorld();
    return 0;
}

```

## Parâmetros

Parâmetros são valores que são passados para uma função. Parâmetros são definidos entre parênteses após o nome da função.

```cpp

void printNumber(int x){
    std::cout << x << std::endl;
}

int main(){
    printNumber(5);
    return 0;
}

```

## Retornando um valor

Uma função pode retornar um valor. Um valor é retornado com a palavra-chave `return`.

```cpp

int add(int x, int y){
    return x + y;
}

int main(){
    std::cout << add(5, 10) << std::endl;
    return 0;
}

```

# Arrays

Arrays são usados para armazenar uma lista de valores. Existem duas formas de definir um array, onde a primeira, ela é declarada já com seus valores inseridos, e a segunda, ela é declarada sem valores, porém, com um tamanho definido.

```cpp

int array1[] = {1, 2, 3, 4, 5};

int array2[5];
array2[0] = 1;
array2[1] = 2;
array2[2] = 3;
array2[3] = 4;
array2[4] = 5;

```

Vale lembrar que, apesar do index dos elementos serem contados a partir do 0, o tamanho da array é definido com base na quantidade total de elementos, e não no index do último elemento.

Outra informação importante sobre as arrays é que, assim como uma variável, uma array também recebe um tipo específico de dados, e só pode armazenar valores do mesmo tipo.

## Acessando elementos

Os elementos de um array são acessados com o nome da array e o index do elemento entre colchetes.

```cpp

int array[] = {1, 2, 3, 4, 5};

std::cout << array[0] << std::endl;

```

## Tamanho de uma array

O tamanho de uma array é obtido com a função `sizeof`. Esta função retorna o tamanho em bytes de um tipo de dado, ou de uma array.

```cpp

int array[] = {1, 2, 3, 4, 5};

std::cout << sizeof(array) << std::endl;
std::cout << sizeof(int) << std::endl;
std::cout << sizeof(array) / sizeof(int) << std::endl;

```

## Passando uma array para uma função

Uma array pode ser passada para uma função como parâmetro, e a função pode acessar os elementos da array. Porém, vale notar que, ao ser passada para uma função, uma array não é copiada, e sim, é passada por referência, e o seu tamanho também não é passado. Ou seja, para acessar os elementos de uma array passada para uma função, é necessário passar o tamanho da array como parâmetro.

```cpp

void printArray(int array[], int size){
    for(int i = 0; i < size; i++){
        std::cout << array[i] << std::endl;
    }
}

int main(){
    int array[] = {1, 2, 3, 4, 5};
    tamanho = sizeof(array) / sizeof(int);
    printArray(array, tamanho);
    return 0;
}

```

## Arrays multidimensionais

Arrays multidimensionais são arrays que possuem mais de uma dimensão. Arrays multidimensionais são definidas com mais de um par de colchetes.

```cpp

std::string carros[][3] = {{"Detomasso", "Ferrari", "Lamborghini"},
                           {"Ford", "Chevrolet", "Dodge"},
                           {"Bugatti", "Koenigsegg", "Pagani"}};

std::cout << carros[0][0] << std::endl;
std::cout << carros[0][1] << std::endl;
std::cout << carros[0][2] << std::endl;

std::cout << carros[1][0] << std::endl;
std::cout << carros[1][1] << std::endl;
std::cout << carros[1][2] << std::endl;

std::cout << carros[2][0] << std::endl;
std::cout << carros[2][1] << std::endl;
std::cout << carros[2][2] << std::endl;

```

