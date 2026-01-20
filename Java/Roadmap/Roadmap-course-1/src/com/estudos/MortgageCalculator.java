package com.estudos;

import java.util.Locale;
import java.util.Scanner;

public class MortgageCalculator {
    void mortgageCalculator(){
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ENGLISH);
        System.out.print("How much do you want to loan? ");
        int loan = scanner.nextInt();
        System.out.print("What's the annual interest rate? ");
        float interest = scanner.nextFloat();
        System.out.print("For how many years do you wat to pay? ");
        int period = scanner.nextInt();
        System.out.println(" ");

        float mensalInterest = (interest / 100)/12;
        int numberOfPayments = period * 12;
        System.out.println(mensalInterest);
        System.out.println(numberOfPayments);

        System.out.println("System variables for debug:");
        float top = (float) Math.pow(1+mensalInterest, numberOfPayments) * mensalInterest;
        System.out.println(top);
        float bottom = (float) Math.pow(1+mensalInterest, numberOfPayments) - 1;
        System.out.println(bottom);
        float mortgage = loan*(top/bottom);

        System.out.println(" ");

        System.out.println("Mortgage: " + mortgage);
        System.out.println("Total: " + mortgage*numberOfPayments);
    }
}
