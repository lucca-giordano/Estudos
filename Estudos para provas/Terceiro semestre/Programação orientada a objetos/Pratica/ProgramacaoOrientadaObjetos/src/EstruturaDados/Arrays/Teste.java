package EstruturaDados.Arrays;

public class Teste {

    public static void main(String[] args){

        int[] numeros = new int[5];

        for (int i = 0; i <= 4; i++){
            numeros[i] = i * i;
        }

        for (int i = 0; i <= 4; i++){
            System.out.println("Numero " + i + " é igual a: " + numeros[i]);
        }


    }

}
