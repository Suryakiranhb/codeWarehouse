package com.practice.methods.messingabout;
import java.util.Scanner;

public class Tables {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number you want the tables of");
        int num = sc.nextInt();
        for(int i=1; i<=10; i++) {
            System.out.println(num+" x " +i+ " = " +(num*i));
        }
        sc.close();
    }
}