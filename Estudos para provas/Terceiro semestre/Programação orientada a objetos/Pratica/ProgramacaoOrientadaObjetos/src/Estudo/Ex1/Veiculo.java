package Estudo.Ex1;

public class Veiculo implements Vendavel{

    private String modelo;
    private int anoFabricacao;
    private double preco;
    private boolean disponivel;

    public Veiculo(String modelo, int anoFabricacao, double preco, boolean disponivel) {
        this.modelo = modelo;
        this.anoFabricacao = anoFabricacao;
        this.preco = preco;
        this.disponivel = disponivel;
    }

    public String getModelo(){
        return modelo;
    }

    public int getAnoFabricacao(){
        return anoFabricacao;
    }

    public double getPreco(){
        return preco;
    }

    public boolean getDisponivel(){
        return disponivel;
    }

    public void setModelo(String modeloSet){
        modelo = modeloSet;
    }

    public void setAnoFabricacao(int anoFabricacaoSet){
        anoFabricacao = anoFabricacaoSet;
    }

    public void setPreco(double precoSet){
        preco = precoSet;
    }

    public void setDisponivel(boolean disponivelSet){
        disponivel = disponivelSet;
    }


    @Override
    public void vender() {
        System.out.println("Veiculo vendido: " + modelo);
    }
}
