package Estudo.Ex1;

public class Carro extends Veiculo{

    private int qtdPortas;

    public Carro(String modelo, int anoFabricacao, double preco, boolean disponivel, int qtdPortas) {
        super(modelo, anoFabricacao, preco, disponivel);
        this.qtdPortas = qtdPortas;
    }

    public int getQtdPortas(){
        return qtdPortas;
    }

    public void setQtdPortas(int qtdPortasSet){
        qtdPortas = qtdPortasSet;
    }
}
