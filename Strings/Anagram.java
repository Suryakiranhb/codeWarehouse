package com.practice.surya.messingabout;

import java.util.Scanner;

public class Anagram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the first word: ");
		String word1 = sc.next();
		System.out.println("Enter the second word: ");
		String word2 = sc.next();
		String word1Sorted = sorter(word1);
		String word2Sorted = sorter(word2);
		if(word1Sorted.equals(word2Sorted)) {
			System.out.println("Anagram guaranteed");
		}
		else {
			System.out.println("Not anagram");
		}
	}
	public static String sorter(String str) {
		char[] a =  str.toCharArray();
		for(int i=0; i<=a.length-1; i++) {
			for(int j=i; j<=a.length-1; j++) {
				if(a[j]>a[i]) {
					char temp = a[i];
					a[i] = a[j];
					a[j] = temp;
				}
				else {
					continue;
				}
			}
		}
		String newStr = new String(a);
//		System.out.println(newStr);
		return newStr;
	}
}
