# Java

Aqui estão todas as minhas anotações sobre Java, desde o básico até o avançado.

<!--imagem a ser inserida-->

---

teste

# Sumário

- [O que é Java?](#o-que-é-java)
- [Variáveis](#variáveis)
- [Operadores](#operadores)
- [Entrada e saída de dados](#entrada-e-saída-de-dados)
- [Estruturas de controle](#estruturas-de-controle)
- [Estruturas de repetição](#estruturas-de-repetição)
- [Classes](#classes)
- [Métodos](#métodos)
- [Objetos](#objetos)

---

# O que é Java?

Java é uma linguagem de programação compilada, criada por [James Gosling](https://www.google.com/search?client=opera-gx&hs=JTc&sxsrf=AJOqlzVHGl4MoG_a2wYaqCDb8ksAguYEeg:1677563857638&q=James+Gosling&stick=H4sIAAAAAAAAAONgVuLQz9U3SMkzjH_EaMwt8PLHPWEprUlrTl5jVOHiCs7IL3fNK8ksqRQS42KDsnikuLjgmngWsfJ6JeamFiu45xfnZOalAwAtXGcjUgAAAA&sa=X&ved=2ahUKEwir_cmuxLf9AhUPGLkGHb3DBJEQzIcDKAB6BAgmEAE), com o objetivo de ser uma linguagem de programação orientada a objetos. Java é uma linguagem de programação muito popular, sendo usada em diversos sistemas operacionais, como Windows, Linux e Mac OS. Java é uma linguagem de programação muito poderosa, sendo usada em diversos sistemas, como Android, Minecraft, Spotify, Netflix, entre outros.

# Variáveis

Assim como em toda linguagem de programação, em Java também é possível declarar variáveis. Uma variável é um espaço na memória do computador que pode ser usado para armazenar dados. Para declarar uma variável em Java, basta usar a seguinte sintaxe:

```java
tipo nomeDaVariavel;
```

Dessa forma, entramos nos tipos de variáveis. Existem 8 tipos de variáveis em Java:

- `byte`: armazena números inteiros de -128 a 127;
- `short`: armazena números inteiros de -32.768 a 32.767;
- `int`: armazena números inteiros de -2.147.483.648 a 2.147.483.647;
- `long`: armazena números inteiros de -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807;
- `float`: armazena números decimais de 3.402.823.5 E+38 a 1.4 E-45;
- `double`: armazena números decimais de 1.797.693.134.862.315.7 E+308 a 4.9 E-324;
- `char`: armazena um único caractere, como letras, números e símbolos;
- `boolean`: armazena valores lógicos, como `true` e `false`.

Dessa forma, vamos declarar uma variável de cada tipo:

```java
byte idade = 18;
short ano = 2021;
int numero = 123456789;
long numeroGrande = 1234567890123456789L;
float numeroDecimal = 123.456F;
double numeroGrandeDecimal = 123.4567890123456789;
char letra = 'A';
boolean verdadeiro = true;
```

# Operadores

Operadores são símbolos que realizam operações matemáticas, lógicas e de atribuição. Em Java, existem 5 tipos de operadores:

- Aritméticos: `+`, `-`, `*`, `/`, `%`:
    - `+` é o operador de adição, que soma dois valores;
    - `-` é o operador de subtração, que subtrai dois valores;
    - `*` é o operador de multiplicação, que multiplica dois valores;
    - `/` é o operador de divisão, que divide dois valores;
    - `%` é o operador de módulo, que retorna o resto da divisão entre dois valores;

- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`:
    - `==` é o operador de igualdade, que retorna `true` se os dois valores forem iguais;
    - `!=` é o operador de diferença, que retorna `true` se os dois valores forem diferentes;
    - `>` é o operador de maior que, que retorna `true` se o primeiro valor for maior que o segundo;
    - `<` é o operador de menor que, que retorna `true` se o primeiro valor for menor que o segundo;
    - `>=` é o operador de maior ou igual a, que retorna `true` se o primeiro valor for maior ou igual ao segundo;
    - `<=` é o operador de menor ou igual a, que retorna `true` se o primeiro valor for menor ou igual ao segundo;

- Lógicos: `&&`, `||`, `!`:
    - `&&` é o operador de conjunção, que retorna `true` se os dois valores forem `true`;
    - `||` é o operador de disjunção, que retorna `true` se um dos valores for `true`;
    - `!` é o operador de negação, que retorna o valor oposto do valor passado;

- Atribuição: `=`, `+=`, `-=`, `*=`, `/=`, `%=`:
    - `=` é o operador de atribuição, que atribui um valor a uma variável;
    - `+=` é o operador de atribuição aditiva, que adiciona um valor a uma variável;
    - `-=` é o operador de atribuição subtrativa, que subtrai um valor de uma variável;
    - `*=` é o operador de atribuição multiplicativa, que multiplica um valor por uma variável;
    - `/=` é o operador de atribuição divisiva, que divide um valor por uma variável;
    - `%=` é o operador de atribuição modular, que atribui o resto da divisão entre dois valores a uma variável;
- Incremento e decremento: `++`, `--`: 
    - `++` é o operador de incremento, que adiciona 1 ao valor da variável;
    - `--` é o operador de decremento, que subtrai 1 do valor da variável;

# Entrada e saída de dados

Para ler dados do teclado, podemos usar a classe `Scanner`. Para isso, precisamos criar um objeto da classe `Scanner` e passar o `System.in` como parâmetro:

```java
Scanner scanner = new Scanner(System.in);
```

Agora, podemos usar o método `nextLine()` para ler uma linha inteira do teclado:

```java
String nome = scanner.nextLine();
```

Para imprimir dados na tela, podemos usar o método `System.out.println()`:

```java
System.out.println("Olá, mundo!");
```

# Estruturas de controle

A estrutura condicional é usada para executar um bloco de código se uma condição for verdadeira. Em Java, existem duas estruturas condicionais: `if` e `switch`.

## if

A estrutura `if` é usada para executar um bloco de código se uma condição for verdadeira. Para isso, basta usar a seguinte sintaxe:

```java
if (condicao) {
    // bloco de código
}
```

Também é possível usar a estrutura `if` com o `else`, que executa um bloco de código se a condição for falsa:

```java
if (condicao) {
    // bloco de código
} else {
    // bloco de código
}
```

E também é possível usar a estrutura `if` com o `else if`, que executa um bloco de código se a condição for falsa e outra condição for verdadeira:

```java
if (condicao) {
    // bloco de código
} else if (condicao) {
    // bloco de código
} else if (condicao) {
    // bloco de código
} else {
    // bloco de código
}
```

## switch

A estrutura `switch` é usada para executar um bloco de código de acordo com o valor de uma variável. Para isso, basta usar a seguinte sintaxe:

```java
switch (variavel) {
    case valor1:
        // bloco de código
        break;
    case valor2:
        // bloco de código
        break;
    case valor3:
        // bloco de código
        break;
    default:
        // bloco de código
        break;
}
```

# Estruturas de repetição

A estrutura de repetição é usada para executar um bloco de código várias vezes. Em Java, existem três estruturas de repetição: `while`, `do while` e `for`.

## while

A estrutura `while` é usada para executar um bloco de código enquanto uma condição for verdadeira. Para isso, basta usar a seguinte sintaxe:

```java
while (condicao) {
    // bloco de código
}
```

## do while

A estrutura `do while` é usada para executar um bloco de código enquanto uma condição for verdadeira. A diferença entre a estrutura `do while` e a estrutura `while` é que a estrutura `do while` executa o bloco de código pelo menos uma vez. Para isso, basta usar a seguinte sintaxe:

```java
do {
    // bloco de código
} while (condicao);
```

## for

A estrutura `for` é usada para executar um bloco de código uma quantidade determinada de vezes. A estrutura `for` possui três partes: uma inicialização, uma condição e uma atualização. Para isso, basta usar a seguinte sintaxe:

```java
for (inicializacao; condicao; atualizacao) {
    // bloco de código
}
```

Como por exemplo:

```java
for (int i = 0; i < 10; i++) {
    // bloco de código
}
```

# Classes

Em Java, uma classe é um modelo que define os atributos e métodos de um objeto. Para criar uma classe, basta usar a seguinte sintaxe:

```java
public class NomeDaClasse {
    // atributos
    // métodos
}
```

## Atributos

Os atributos são as características de um objeto. Para criar um atributo, basta usar a seguinte sintaxe:

```java
public class NomeDaClasse {
    // atributos
    public tipo nome;
    // métodos
}
```

## Métodos

Os métodos são as ações de um objeto. Para criar um método, basta usar a seguinte sintaxe:

```java
public class NomeDaClasse {
    // atributos
    // métodos
    public tipo nome() {
        // bloco de código
    }
}
```

# Objetos

Um objeto é uma instância de uma classe. Para criar um objeto, basta usar a seguinte sintaxe:

```java
NomeDaClasse objeto = new NomeDaClasse();
```