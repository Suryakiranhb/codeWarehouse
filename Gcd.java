package com.practice.methods.gcd;

import java.util.Scanner;

public class Gcd {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the two numbers: ");
		int a = sc.nextInt();
		int b = sc.nextInt();
		Gcdfind res = new Gcdfind();
		int ans = res.gcdfinder(a, b);
		System.out.println("The GCD of the two numbers "+a+" and "+b+" is: " +ans);
	}
}	
