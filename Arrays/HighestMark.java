package com.practice.tekstac.arrays;

import java.util.Scanner;

public class HighestMark {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		System.out.println("How many numbers?");
//		int num = sc.nextInt();
		int num = 6;
		int[] a = new int[num];
//		System.out.println("Enter the numbers");
		for(int i=0; i<=num-1; i++) {
			a[i] = sc.nextInt();
			if(a[i]<0) {
				System.out.println("Invalid Mark");
				System.exit(i);
			}
		}
		int highest = a[0];
		for(int i=1; i<=num-1; i++) {
			if(a[i]>highest) {
				highest = a[i];
			}
		}
		System.out.println("Highest mark is "+highest);
		
		
	}
}
