package com.practice.tekstac.strings;

import java.util.Scanner;

public class ContainsSubstring {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the sentence");
		String sentence = sc.nextLine();
		System.out.println("Enter the substring to find");
//		sc.nextLine();
		String substring = sc.nextLine();
//		sc.nextLine();
		if(sentence.contains(substring)) {
			System.out.println(substring+ " is contained in the sentence.");
		}
		else {
			System.out.println(substring+" is not contained in the sentence.");
		}
		sc.close();
	}
}
