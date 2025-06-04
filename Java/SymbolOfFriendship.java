package com.practice.methods.messingabout;

import java.util.Scanner;

public class SymbolOfFriendship {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a number for John");
		int john = sc.nextInt();
		if (john>=100 && john<=20000) {
			System.out.println("Enter a number for James");
			int james = sc.nextInt();
			int count =0;
			if(james>john && james>=100 && james<=20000) {
				for(int i=1; i<james; i++) {
					if(john%i==0) {
						if(i==john) {
							continue;
						}
						else {
							System.out.println(i);
							count = count+i;							
						}
					}
				}
				if(count == james) {
					System.out.println("Symbol of friendship");
				}
				else {
					System.out.println("May be a good friend");
				}
		}
		else {
			System.out.println("Invalid number");
		}
	}
		else {
			System.out.println("Invalid number");
		}
		sc.close();
	}
}
