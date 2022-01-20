package com.practice.tekstac.arrays;

import java.util.Scanner;

public class ArrayReverse {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the array size");
		int size = sc.nextInt();
		int[] a = new int[size];
		System.out.println("Enter the values");
		for(int i=0; i<=size-1; i++) {
			a[i] = sc.nextInt();
		}
		for(int i=size-1; i>=0; i--) {
			System.out.println(a[i]);
		}
	}
}
