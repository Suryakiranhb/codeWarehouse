package com.practice.tekstac.strings;

import java.util.Scanner;

public class Characters {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the string");
		String sentence = sc.nextLine();
		char[] a = sentence.toCharArray();
		int count = 0;
		for(int i=0; i<=a.length-1; i++) {
			if(a[i]!=' ') {
				count++;
			}
		}
		System.out.println(count);
		sc.close();		
	}
}
