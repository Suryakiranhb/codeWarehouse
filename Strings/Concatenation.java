package com.practice.tekstac.strings;

import java.util.Scanner;

public class Concatenation {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter string 1: ");
		String s1 = sc.nextLine();
		System.out.print("Enter string 2: ");
		String s2 = sc.nextLine();
		String s3 = s1.concat(" "+s2);
		System.out.println(s3);
		sc.close();
	}
}
