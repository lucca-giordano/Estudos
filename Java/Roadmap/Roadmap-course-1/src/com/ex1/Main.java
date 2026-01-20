package com.ex1;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Task> tasks = new ArrayList<>();
        byte option;

        System.out.println("Bem vindo ao sistema de tarefas. Escolha uma das opções abaixo:");

        LOOP:
        while(true){
            System.out.println("""
                1 - Criar nova tarefa
                2 - Listar as tarefas
                3 - Concluir uma tarefa
                4 - Sair do sistema""");

            option = scanner.nextByte();
            scanner.nextLine();

            switch (option) {
                case 1:
                    System.out.print("Digite o título da tarefa: ");
                    String title = scanner.nextLine();

                    System.out.print("Digite a descrição da tarefa: ");
                    String description = scanner.nextLine();

                    System.out.print("Digite a data de inicio da tarefa: ");
                    String startDate = scanner.nextLine();

                    System.out.print("Digite a data de término da tarefa: ");
                    String endDate = scanner.nextLine();

                    tasks.add(new Task(title, description, startDate, endDate));
                    break;

                case 2:
                    System.out.println(" ");
                    for(int i = 0; i < tasks.size(); i++){
                        Task t = tasks.get(i);
                        System.out.println(i+1 + " - " + t.title + ": " + (t.isTaskComplete ? "Concluída" : "Não concluída"));
                    }
                    System.out.println(" ");
                    break;

                case 3:
                    System.out.print("Insira o número da tarefa: ");
                    int n = scanner.nextInt();
                    tasks.get(n - 1).concluir();
                    break;

                case 4:
                    break LOOP;
            }
        }

    }

}
