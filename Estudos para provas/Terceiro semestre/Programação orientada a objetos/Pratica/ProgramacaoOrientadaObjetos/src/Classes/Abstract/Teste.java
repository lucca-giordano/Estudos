package Classes.Abstract;

public class Teste {

    public static void main(String[] args){

        Carro carro = new Carro();
        // Veiculo veiculo = new Veiculo();
        // Erro, pois veiculo é abstrato, porém Carro pode herdar essa classe.

        carro.andar();


    }

}
