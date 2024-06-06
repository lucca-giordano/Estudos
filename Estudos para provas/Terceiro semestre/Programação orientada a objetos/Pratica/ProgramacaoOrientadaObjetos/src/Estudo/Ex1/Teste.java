package Estudo.Ex1;

public class Teste {

    public static void main(String[] args){

        Carro carro1 = new Carro("Honda Fit", 2005, 23000, true, 4);
        Moto moto1 = new Moto("Honda biz", 2010, 12, true, 110);
        Pessoa pessoa1 = new Pessoa("Joao", carro1);

        System.out.println("Modelo: " + pessoa1.getVeiculo().getModelo());
        pessoa1.setVeiculo(moto1);
        System.out.println("Modelo: " + pessoa1.getVeiculo().getModelo());


    }

}
