package com.practice.methods.gcd;

import java.util.Scanner;

public class Factorial {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the factorial of the number you want to find: ");
		int num = sc.nextInt();
//		int ans = 1;
		int ans=1;
		
//DECREMENTAL STYLE
		for(int i=num; i>0; i--) {
			ans = ans*i;
		}
//INCREMENTAL STYLE
//		for(int i=1; i<=num; i++) {
//			j = j*i;
//		}
		
		System.out.println("The factorial is "+ans);
	}
}
