package EstruturaDados.Tempo;

public class Teste {

    public static void main(String[] args){
        long inicio = System.currentTimeMillis();

        long n = 100;
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }

        long fim = System.currentTimeMillis();

        long tempo = fim - inicio;

    }

}
