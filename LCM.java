package com.practice.methods.messingabout;

import java.util.Scanner;

public class LCM {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the first number");
		int num1 = sc.nextInt();
		System.out.println("Enter the second number");
		int num2 = sc.nextInt();
		int smaller = 0;
		if (num1<num2) {
			smaller = num1;
		}
		else {
			smaller = num2;
		}
		int lcm=1;
		for(int i=1; i<=smaller; i++) {
			if(num1%i ==0 && num2%i==0) {
				lcm = i;
			}
		}
		System.out.println("GCD: "+lcm);
		lcm = num1/lcm;
		lcm = lcm*num2;
		System.out.println("LCM:"+lcm);
		sc.close();
	}
}
