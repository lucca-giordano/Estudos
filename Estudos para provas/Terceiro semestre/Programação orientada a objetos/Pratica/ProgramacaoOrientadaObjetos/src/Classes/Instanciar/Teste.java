package Classes.Instanciar;

public class Teste {
        public static void main(String[] args) {

            Curso curso1 = new Curso("Java", "A", 10);
            Curso curso2 = new Curso("Python", "B", 20);

            Gato gato1 = new Gato("Mingau", "Siames", "Branco", 5, 3);
            Gato gato2 = new Gato("Frajola", "Persa", "Cinza", 4, 2);

            System.out.println(curso1.nome);
            System.out.println(curso2.nome);
            System.out.println(gato1.nome);
            System.out.println(gato2.nome);
    }
}
