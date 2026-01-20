package com.estudos;

public class Main {
    public static void main(String[] args) {
        String[] fruits = {"Apple", "Banana", "Orange"};
        for(int i = 0; i< fruits.length; i++){
            System.out.println(fruits[i]);
        }

        for(String fruit: fruits){
            System.out.println(fruit);
        }

    }
}