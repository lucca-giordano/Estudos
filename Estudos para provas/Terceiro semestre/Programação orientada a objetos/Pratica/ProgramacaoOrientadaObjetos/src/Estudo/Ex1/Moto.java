package Estudo.Ex1;

public class Moto extends Veiculo{

    private int qtdCilindradas;

    public Moto(String modelo, int anoFabricacao, double preco, boolean disponivel, int qtdCilindradas) {
        super(modelo, anoFabricacao, preco, disponivel);
        this.qtdCilindradas = qtdCilindradas;
    }

    public int getQtdCilindradas(){
        return qtdCilindradas;
    }

    public void setQtdCilindradas(int qtdCilindradasSet){
        qtdCilindradas = qtdCilindradasSet;
    }

}
