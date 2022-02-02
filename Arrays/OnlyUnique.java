package com.practice.surya.messingabout;
import java.util.Scanner;

public class OnlyUnique {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter the string");
		String str = sc.nextLine();
		char[] a = str.toCharArray();
		for(int i=0; i<=a.length-1; i++) {
			for(int j=i+1; j<=a.length-1; j++) {
				if(a[i]==' ') {
					continue;
				}
				else if(a[i] == a[j]) {
					a[j] = '-';
				}
			}
		}
			String nonRepeat = new String(a);
			nonRepeat = nonRepeat.replace("-", "");
			System.out.println(nonRepeat);
 	}
}
