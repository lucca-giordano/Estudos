package EstruturaDados.Espaco;

public class Teste {

    public static void main(String[] args){
        int n = 1234;
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = i;
        }

        int bits = array.length * Integer.SIZE;
        int bytes = array.length * Integer.BYTES;

        System.out.println("Quantidade de bits: " + bits);
        System.out.println("Quantidade de bytes: " + bytes);
    }

}
