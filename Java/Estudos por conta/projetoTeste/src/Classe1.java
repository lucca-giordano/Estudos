/*
 * Classes são como se fossem os arquivos .java, onde você pode ter várias classes em um mesmo projeto.
 * 
 * No java, você pode ter classes diferentesm mas que estão no mesmo pacote, e que podem se comunicar.
 * Para isso, em uma de suas classes você cria um método, e na outra você chama esse método.
 * 
 * Para chamar um método de outra classe, você precisa criar um objeto dessa classe, e chamar o método
 * desse objeto.
 * 
 * Para criar um objeto, você precisa usar a palavra reservada new, e depois o nome da classe.
 * Dessa forma, criar um objeto de uma classe que se chama "Classe2" ficaria assim:
 * 
 * Classe2 c2 = new Classe2();
 * 
 * sendo que c2 é o nome do objeto, e Classe2 é o nome da classe.
 * 
 * É preciso repetir o nome da "Classe2" duas vezes, pois a primeira é para criar o objeto, 
 * e a segunda é para chamar o método.
 */

public class Classe1 {
    
    public static void main(String[] args) {
        
        Classe2 c2 = new Classe2();

        int vida = 10;

        System.out.println("Vida: " + vida);

        vida = c2.perderVida(vida);

        System.out.println("Vida: " + vida);

        vida = c2.ganharVida(vida);

        System.out.println("Vida: " + vida);

    }

}
