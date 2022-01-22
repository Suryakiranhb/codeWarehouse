package com.practice.tekstac.arrays;

import java.util.Scanner;

public class MakeNumber {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of the array");
		int size = sc.nextInt();
		if(size<=0) {
			System.out.println("Invalid array size");
			return;
		}
		else {
			int[] a = new int[size];
			System.out.println("Enter the array elements");
			for(int i=0; i<=size-1; i++) {
				a[i] = sc.nextInt();
			}
			int flag = 0;
			for(int i=0; i<=size-1; i++) {
				if(a[i]<10 && a[i]%2==0) {
	//				if(a[i]%2==0) {
						System.out.print(a[i]);
						flag=1;
					}
				}
		//	}
			if(flag == 0) {
				System.out.println("Single digit even number is not found in the array");
			}
		}
	}
}
