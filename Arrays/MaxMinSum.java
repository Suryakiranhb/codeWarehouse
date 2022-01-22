package com.practice.tekstac.arrays;

import java.util.Scanner;

public class MaxMinSum {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of an array:");
		int size = sc.nextInt();
		if (size <= 0) {
			System.out.println("Invalid Array Size");
		} else {
			int[] a = new int[size];
			System.out.println("Enter the elements:");
			for (int i = 0; i <= size - 1; i++) {
				a[i] = sc.nextInt();
			}
			int max = a[0];
			int min = a[0];
			for (int i = 0; i <= size - 1; i++) {
				if (a[i] > max) {
					max = a[i];
				}
				if (a[i] < min) {
					min = a[i];
				}
			}
			System.out.println("Maximum element: " + max + "\nMinimum element: " + min + "\nSum: " + (max + min));
		}
	}
}
