package Classes.Heranca;

public class Pessoa {

    public String nome, sobrenome;
    public int idade, cpf;

    public void entrou(){
        System.out.println(this.nome + " chegou na escola!");
    }

    public void saiu(){
        System.out.println(this.nome + " saiu da escola!");
    }

}
