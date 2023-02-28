/*
 * O java é uma linguagem fortemente tipada, ou seja, todas as variáveis devem ser declaradas
 * Temos no total, 8 tipos de variáveis, e esses são os nomes e a declaração de cada uma delas:
 * 
 * byte: 8 bits - numeros inteiros de -128 a 127 ou de 0 a 255
 * short: 16 bits - numeros inteiros de -32768 a 32767 ou de 0 a 65535
 * int: 32 bits - numeros inteiros de -2147483648 a 2147483647 ou de 0 a 4294967295
 * long: 64 bits - numeros inteiros de -9223372036854775808 a 9223372036854775807 ou de 0 a 18446744073709551615
 * float: 32 bits - mesmo tamanho do int, mas com casas decimais
 * double: 64 bits - mesmo tamanho do long, mas com casas decimais
 * char: 16 bits - caracteres
 * boolean: 1 bit - true ou false
 * 
 * Em java, as srings são objetos, e não variáveis, por isso não entram nessa lista
 * 
 */

public class variaveis {
    public static void main(String[] args) {
        // Declaração de variáveis

        byte b = 127;
        short s = 32767;
        int i = 2147483647;
        long l = 9223372036854775807L;
        float f = 3.14f;
        double d = 3.14;
        char c = 'a';
        boolean bo = true;

        String nome = "João";

        // Imprimindo as variáveis
        System.out.println("byte: " + b);
        System.out.println("short: " + s);
        System.out.println("int: " + i);
        System.out.println("long: " + l);
        System.out.println("float: " + f);
        System.out.println("double: " + d);
        System.out.println("char: " + c);
        System.out.println("boolean: " + bo);
        System.out.println("String: " + nome);
        
    }
}
