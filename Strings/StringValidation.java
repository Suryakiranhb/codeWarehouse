package com.practice.tekstac.strings;

import java.util.Scanner;

public class StringValidation {
	public static void main(String[] args) {
		Scanner	sc = new Scanner(System.in);
		System.out.println("Enter string");
		String str = sc.nextLine();
		if(str.matches("[ a-zA-Z ]+")) {
			int len = str.length();
			System.out.println("No of characters is: "+len);
		}
		else {
			System.out.println("Invalid Strings");
		}
		sc.close();
	}
}
