package com.practice.tekstac.strings;

import java.util.Scanner;

public class Splitter {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the string");
		String string = sc.nextLine();
		System.out.println("How do you want it? 1. Manual or 2. In-built method");
		int choice = sc.nextInt();
		if(choice == 1) {
			char[] a = string.toCharArray();
			System.out.println("Enter what to split it with");
			char split = sc.next().charAt(0);
			for(int i=0; i<=a.length-1; i++) {
				if(a[i] == split) {
					i++;
					System.out.println();
				}
				System.out.print(a[i]);
			}
		}
		else {
			System.out.println("Enter what to split it with");
			String split = sc.next();
			String[] a = string.split(split);
			for(int i=0; i<=a.length-1; i++) {
				System.out.println(a[i]);
			}
		}
		sc.close();
	}
}
