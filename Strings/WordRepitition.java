package com.practice.methods.messingabout;

import java.util.Scanner;

public class WordRepitition {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the String:");
		String s1 = sc.next();	
		sc.nextLine();
		System.out.println("Enter the sentence:");
		String s2 = sc.nextLine();
		s2 = s2.replace(".", " .");
		s2 = s2.replace(",", " ,");
		s2 = s2.replace("\"", "\" \"");
//		s2 = s2.replace("[a-zA-Z+—a-zA-Z+]", " — ");
//		s2 = s2.replace("[0-9+—a-zA-Z+]", " — ");
		s2 = s2.replace("(", "( ");
		s2 = s2.replace(")", " )");
		s2 = s2.replace(":", " :");
		s2 = s2.replace("?", " ?");
		String[] a = s2.split(" ");
//		System.out.println("Pre-processed string:");
//		for(int i=0; i<=a.length-1; i++) {
//			System.out.print(a[i]+" ");
//		} 
//		System.out.println();
		int count =0;
//		System.out.println(a[3]);
//		for(int i=0; i<=a.length-1; i++) {
//			if(a[i].matches("[a-zA-Z+.$]")) {
//				System.out.println(a[i]);
//				a[i] = a[i].replace("."," ");
//				System.out.println(a[i]);
//			}
//		}
		for(int i=0; i<=a.length-1; i++) {
			if(a[i].equalsIgnoreCase(s1)) {
				count++;
//				System.out.println(a[i]);
			}
		}
		System.out.println(count);
	} 
}