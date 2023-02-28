/*
 * Assim como em toda linguagem de programação, o Java também possui estruturas de repetição,
 * que são utilizadas para repetir uma ação várias vezes.
 * 
 * Estruturas de repetição são conhecidas como loops, seu funcionamento gira em torno de
 * uma condição, que pode ser verdadeira ou falsa, e dependendo do resultado dessa condição,
 * o programa irá executar uma ação ou outra.
 * 
 * No Java, temos várias estruturas de repetição, porém vamos começar com as mais básicas:
 * 
 * while: executa uma ação enquanto a condição for verdadeira
 * do while: executa uma ação pelo menos uma vez, e enquanto a condição for verdadeira
 * for: executa uma ação uma quantidade determinada de vezes
 * 
 */

public class loops {
    public static void main(String[] args) {
        
        int contadorWHILE = 0;

        while(contadorWHILE < 10) {
            System.out.println(contadorWHILE);
            contadorWHILE++;
        }

        int contadorDOWHILE = 0;

        do {
            System.out.println(contadorDOWHILE);
            contadorDOWHILE++;
        } while(contadorDOWHILE < 10);

        for(int contadorFOR = 0; contadorFOR < 10; contadorFOR++) {
            System.out.println(contadorFOR);
        }
        
        // Nos 3 casos, o resultado será o mesmo.

    }
}
