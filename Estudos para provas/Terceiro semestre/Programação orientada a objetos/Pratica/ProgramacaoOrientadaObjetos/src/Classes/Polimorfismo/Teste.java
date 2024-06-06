package Classes.Polimorfismo;

public class Teste {

    public static void main(String[] args){
        Animal animal1 = new Gato();
        Animal animal2 = new Cachorro();

        animal1.emitirSom();
        animal2.emitirSom();

    }

}
