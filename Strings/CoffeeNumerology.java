package com.practice.methods.messingabout;

import java.util.Scanner;

public class CoffeeNumerology {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Staff Name");
		String name = sc.nextLine();
//		name = name.replace(" ", "");
		System.out.println(name);
		if(name.matches("[a-zA-z ]+")) {
			int len = name.length();
			System.out.println(len);
			if(len%2==0) {
				System.out.println(name+" satisfies the numerology logic");
			}
			else {
				System.out.println(name+" does not satisfy the numerology logic");
			}
		}
		sc.close();
	}
}
