package com.practice.tekstac.arrays;

import java.util.Scanner;

public class SortArray {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the array size");
		int size = sc.nextInt();
		int[] a = new int[size];
		System.out.println("Enter the values");
		for(int i=0; i<=size-1; i++) {
			a[i] = sc.nextInt();
		}
		//sorting using bubble sort
		for(int i=0; i<=size-1; i++) {
			for(int j=i+1; j<=size-1; j++) {
				if(a[j]<a[i]) { //change sign from < to > to make it sort in descending order
					int temp = a[j];
					a[j] = a[i];
					a[i] = temp;
				}
			}
		}
		//displaying sorted array
		for(int i=0; i<=size-1; i++) {
			System.out.println(a[i]);
		}
	}
}
