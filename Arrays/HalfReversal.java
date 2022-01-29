package com.practice.surya.messingabout;

import java.util.Scanner;

public class HalfReversal {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the word");
		String word = sc.next();
		if(word.length()%2!=0) {
			int max = (word.length()/2)-1;
			char[] wordhalf = word.toCharArray();
			for(int i=0; i<=max-1; i++) {
				if(i<(max-i)) {
				char temp = wordhalf[i];
				wordhalf[i] = wordhalf[max-i];
				wordhalf[max-i] = temp;
			}
				else {
					break;
				}
			}
			String wordhf = new String(wordhalf);
			System.out.println(wordhf);
		}
		else {
			char[] rev = word.toCharArray();
			for(int i=0; i<=rev.length-1; i++) {
				if(i<rev.length-i-1) {
					char temp = rev[i];
					rev[i] = rev[rev.length-i-1];
					rev[rev.length-i-1] = temp;
				}
				else {
					break;
				}
			}
			String reversed = new String(rev);
			System.out.println(reversed);
		}
		sc.close();
	}
}
