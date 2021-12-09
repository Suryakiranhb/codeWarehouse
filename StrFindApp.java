package com.practice.methods.gcd;

import java.util.Scanner;

public class StrFindApp {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the string: ");
			String str = sc.nextLine();
			System.out.println("Enter the character to search for: ");
			char chr = sc.next().charAt(0);
			StrFinder s = new StrFinder();
			boolean presence = s.check(str, chr);
			if(presence == true) {
				System.out.println("The letter "+chr+" is present in "+str);
			}
			else {
				System.out.println("The letter "+chr+" is not present in "+str);
			}
		}
}
