package com.practice.tekstac.arrays;

import java.util.Scanner;

public class Duplicate {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of the array:");
		int size = sc.nextInt();
//		size = size-1;
		if (size <= 0) {
			System.out.println("Invalid array size");
		} 
		else {
			int[] a = new int[size];
			System.out.println("Enter the array elements:");
			for (int i = 0; i <= size - 1; i++) {
				a[i] = sc.nextInt();
			}
			System.out.println("Enter the position of the element to be replicated:");
			int pos = sc.nextInt();
			if (pos > 0 && pos < size) {
				int[] b = new int[size + 1];
				for (int i = 0; i < size ; i++) {
					b[i] = a[i];
				}
				b[size] = a[pos];
				for (int j = 0; j <= b.length - 1; j++) {
					System.out.println(b[j]);
				}
			} 
			else if (pos < 0) {
				System.out.println("Invalid array size");
			} 
			else if (pos > size - 1) {
				System.out.println("Position is greater than the size of the array");
			}
		}
	}
}
