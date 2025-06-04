package com.practice.methods.messingabout;

import java.util.Scanner;

public class Capitalize {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		char[] a = s.toCharArray();
		char c = a[0];
		c = Character.toUpperCase(c);
		a[0] = c; 
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
	}
}
