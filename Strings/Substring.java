package com.practice.tekstac.strings;

import java.util.Scanner;

public class Substring {
	public static void main(String[] args) {
		System.out.println("Enter the string");
		Scanner sc = new Scanner(System.in);
		String string = sc.nextLine();
		System.out.println("Substring, from where to where?");
		int from = sc.nextInt();
		int where = sc.nextInt();
		System.out.println("Which method to use? 1. Manual or 2. Inbuilt method");
		int type = sc.nextInt();
		if(type == 1) {
		char[] a = string.toCharArray();
		for(int i=0; i<=a.length-1; i++ ) {
			if(i>=from && i<where) {
				System.out.print(a[i]);
				}
			}
		}
		else {
			System.out.println(string.substring(from, where));
		}
		sc.close();
	}
}
