package com.ex2;

/*
* Movie: title, rate e watched
* Objetivo: adicionar filme, marcar como assistido, listar filmes, exibir os não assistidos, buscar pelo nome
* */

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        ArrayList<Movie> movies = new ArrayList<>();

        System.out.println("Bem vindo ao sistema de filmes.");

        LOOP:
        while (true){

            System.out.println("""
                    \n
                    Escolha uma das opções abaixo:
                    1 - Adicionar filme
                    2 - Listar todos os filmes
                    3 - Listar os filmes não assistidos
                    4 - Marcar filme como assistido
                    5 - Sair do sistema
                    """);

            byte option = scanner.nextByte();
            scanner.nextLine();

            switch (option){
                case 1: // Adicionar filme
                    while(true){
                        System.out.print("Nome do filme: ");
                        String name = scanner.nextLine();

                        System.out.println("Você já assistiu ao filme? (S/N) ");
                        String response = scanner.nextLine();

                        if(response.equalsIgnoreCase("s")){
                            System.out.println("Qual nota você dá para o filme? (0-10) ");
                            String rate = scanner.nextLine();
                            movies.add(new Movie(name, rate, true));
                        } else {
                            movies.add(new Movie(name, "", false));
                        }

                        System.out.println("Filme adicionado!");

                        System.out.println("Quer adicionar outro filme? (S/N) ");
                        response = scanner.nextLine();

                        if(response.equalsIgnoreCase("n")){
                            break;
                        }

                    }
                    break;

                case 2: // Listar todos os filmes
                    for(int i = 0; i < movies.size(); i++){
                        Movie m = movies.get(i);
                        System.out.println(i+1 + " - " + m.title + " - " + (m.watched ? "Assistido"  + " (" + m.rate  + "/10)" : "Não assistido"));
                    }
                    break;

                case 3: // Listar somente os não assistidos
                    for(int i = 0; i < movies.size(); i++){
                        Movie m = movies.get(i);
                        if(!m.watched){
                            System.out.println(i+1 + " - " + m.title);
                        }
                    }
                    break;

                case 4: // Marcar filme como assistido
                    System.out.println("Insira o número do filme: ");
                    int n = scanner.nextInt();
                    scanner.nextLine();
                    Movie movie = movies.get(n-1);

                    System.out.println("Qual nota você da para o filme: " + movie.title);
                    String rate = scanner.nextLine();

                    movie.markAsWatched();
                    movie.setRating(rate);

                    System.out.println(movie.title + " marcado como assistido, nota: " + movie.rate + "/10");

                    break;

                case 5: // Encerrar o programa
                    System.out.println("\nEncerrando programa.\nAté a próxima!");
                    break LOOP;
            }
        }
    }

}
