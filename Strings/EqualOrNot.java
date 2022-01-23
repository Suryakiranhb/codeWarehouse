package com.practice.tekstac.strings;

import java.util.Scanner;

public class EqualOrNot {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the first string");
		String s1 = sc.nextLine();
		System.out.println("Enter the second string");
		String s2 = sc.nextLine();
		if(s1.equalsIgnoreCase(s2)) {
			if(s1.equals(s2)) {
				System.out.println("Case sensitive match");
			}
			else {
				System.out.println("Case insensitive match");
			}
		}
		else {
			System.out.println("Not equal");
		}
		sc.close();
	}
}
