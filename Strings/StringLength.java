package com.practice.tekstac.strings;

import java.util.Scanner;

public class StringLength {
	public static void main(String[] args) {
		System.out.println("Enter the string");
		Scanner sc = new Scanner(System.in);
		String sentence = sc.nextLine();
		char[] a = sentence.toCharArray();
		int len = a.length;
		if(len%2==0) {
			System.out.println(len+" Even");
		}
		else if(len%2!=0) {
			System.out.println(len+" Odd");
		}
		sc.close();
	}
}
