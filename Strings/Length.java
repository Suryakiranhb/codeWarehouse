package com.practice.tekstac.strings;

import java.util.Scanner;

public class Length {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your name");
		String name = sc.nextLine();
		char[] a = new char[name.length()];
		if(name.matches("[A-Za-z ]+")) {
			int length = name.length();
			System.out.println(name+" has "+(length)+ " characters");
		}
		else {
			System.out.println("Invalid input");
		}
		sc.close();
	}
}
