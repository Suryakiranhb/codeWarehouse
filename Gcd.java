package com.practice.methods.gcd;

import java.util.Scanner;

public class Gcd {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the two numbers: ");
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		while(num2!=0 ) {
			int num3;
			num3=num1%num2;
			num1=num2;
			num2 = num3;
		}
		System.out.println("The GCD of the two numbers is: " +num1);
	}
}
