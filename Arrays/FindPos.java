package com.practice.tekstac.arrays;

import java.util.Scanner;

public class FindPos {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the array size");
		int size = sc.nextInt();
		int[] a = new int[size];
		System.out.println("Enter the values");
		for (int i=0; i<=size-1; i++) {
			a[i] = sc.nextInt();
		}
		System.out.println("Enter the number to find");
		int num = sc.nextInt();
		int flag = 0;
		for (int i=0; i<=size-1; i++) {
			if(a[i] == num) {
				System.out.println(num+" is present in position "+i);
				flag = 1;
			}
		}
		if(flag==0) {
			System.out.println("Number not present");
		}
	}
}
