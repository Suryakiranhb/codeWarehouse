package com.practice.methods.gcd;

import java.util.Scanner;

public class Fibonacci {
public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	System.out.println("Till where do you want the Fibo series to be calculated? ");
	int limit = sc.nextInt();
	int res=0;
	int n1 = 0;
	int n2 = 1;
	int sum = 0;
	System.out.print(n1+" "+n2+" ");
	while(res<limit) {
		res = n1+n2;
		System.out.print((n1+n2)+" ");
		n1 = n2;
		n2 = res;
		sum = sum+res;
	}
	System.out.println("and the Fibo series sum till "+limit+" will be "+(sum+1));
}
}
