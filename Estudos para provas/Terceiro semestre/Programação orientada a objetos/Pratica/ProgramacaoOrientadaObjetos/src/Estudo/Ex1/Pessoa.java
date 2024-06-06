package Estudo.Ex1;

public class Pessoa  {

    private String nome;
    private Veiculo veiculo;

    public Pessoa(String nome, Moto moto){
        this.nome = nome;
        this.veiculo = moto;
    }

    public Pessoa(String nome, Carro carro){
        this.nome = nome;
        this.veiculo = carro;
    }

    public String getNome(){
        return nome;
    }

    public Veiculo getVeiculo(){
        return veiculo;
    }

    public void setNome(String nomeSet){
        nome = nomeSet;
    }

    public void setVeiculo(Veiculo veiculoSet){
        veiculo = veiculoSet;
    }

}