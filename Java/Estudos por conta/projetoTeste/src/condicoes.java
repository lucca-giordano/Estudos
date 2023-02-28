/*
 * Assim como em toda linguagem de programação, o Java também possui estruturas de controle de fluxo,
 * que são utilizadas para controlar o fluxo de execução do programa.
 * 
 * Estruturas de controle de fluxo são conhecidas como condicionais, seu funcionamento gira em torno de 
 * uma condição, que pode ser verdadeira ou falsa, e dependendo do resultado dessa condição, o programa
 * irá executar uma ação ou outra.
 * 
 * No Java, temos várias estruturas de controle de fluxo, porém vamos começar com as mais básicas:
 * 
 * if: executa uma ação se a condição for verdadeira
 * else: executa uma ação se a condição for falsa
 * else if: executa uma ação se a condição for verdadeira, e outra ação se a condição for falsa
 * 
 * Junto a estas estruturas, temos alguns operadores lógicos que são utilizados para comparar valores, esses são:
 * 
 * ==: compara se dois valores são iguais
 * !=: compara se dois valores são diferentes
 * >: compara se um valor é maior que o outro
 * <: compara se um valor é menor que o outro
 * >=: compara se um valor é maior ou igual ao outro
 * <=: compara se um valor é menor ou igual ao outro
 * 
 * Temos também operadores que são utilizados para combinar condições, esses são:
 * 
 * &&: "e" - combina duas condições, e retorna verdadeiro se ambas forem verdadeiras
 * ||: "ou" - combina duas condições, e retorna verdadeiro se uma delas for verdadeira
 * !: "negação" - inverte o resultado de uma condição
 * 
 */

public class condicoes {
    public static void main(String[] args) {
        int idade = 90000000;
        String nome = "João";

        if (idade >= 18 && idade <= 60) {
            System.out.println("Você pode acessar o site");
        }
        else if (idade > 60 || idade < 18) {
            System.out.println("Você não pode acessar o site");
        }

        if (nome.equals("João")) {
            System.out.println("Seu nome é João");
        }
        else {
            System.out.println("Seu nome não é João");
        }
    }
}
