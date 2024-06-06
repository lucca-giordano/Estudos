package Classes.Heranca;

public class Teste {

    public static void main(String[] args){
        Aluno aluno = new Aluno();
        aluno.nome = "João";
        aluno.media = 7;

        System.out.println(aluno.nome);
        aluno.entrou();
        aluno.saiu();


    }
}
