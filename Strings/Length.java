package com.practice.tekstac.strings;

import java.util.Scanner;

public class Length {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your name");
		String name = sc.nextLine();
		char[] a = new char[name.length()];
//		int count = 0;
//		for(int i=0; i<=name.length()-1; i++) {
//			if(a[i] == '\s') {
//				count++;
//			}
//		}
//		for(int i=0; i<=name.length()-1; i++) {
//			System.out.print(a[i]+" ,");
//		}
//		System.out.println(count);
		if(name.matches("[A-Za-z ]+")) {
			int length = name.length();
			System.out.println(name+" has "+(length)+ " characters");
		}
		else {
			System.out.println("Invalid input");
		}
		
	}
}
