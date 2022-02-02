package com.practice.surya.messingabout;

import java.util.Scanner;

public class CaseProduct {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the word/sentence: ");
		String str = sc.nextLine();
		str = str.replace(" ", "");
		System.out.println(str);
		int len = str.length();
		int upper =0, lower =0;
		for(int i=0; i<=len-1; i++) {
			char temp = str.charAt(i);
			if(Character.isUpperCase(temp)) {
				upper++;
			}
			else {
				lower++;
			}
		}
		System.out.println("Uppercase: "+upper+"\nLowercase: "+lower);
		if(upper == 0) {
			upper++;
		}
		if(lower == 0) {
			lower++;
		}
		System.out.println("The product of cases is: "+(upper*lower));
		sc.close();
	}
}
