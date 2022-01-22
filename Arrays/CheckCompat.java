package com.practice.tekstac.arrays;

import java.util.Scanner;

public class CheckCompat {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//first array
		System.out.println("Enter the size for he first array:");
		int size1= sc.nextInt();
		if(size1<=0) {
			System.out.println("Invalid array size");
			return;
		}
			int[] a = new int[size1];
			System.out.println("Enter the elements for the first array:");
			for(int i=0; i<=size1-1; i++) {
				a[i] = sc.nextInt();
			}
		//second array
		System.out.println("Enter the size for the second array:");
		int size2 = sc.nextInt();
		if(size2<=0) {
			System.out.println("Invalid array size");
			return;
		}
			int[] b = new int[size2];
			System.out.println("Enter the elements for the first array:");
			for(int i=0; i<=size2-1; i++) {
				b[i] = sc.nextInt();
			}
		if(size1!=size2) {
			System.out.println("Arrays are Not Compatible");
			return;
		}
			int flag = 0;
			for(int i=0; i<=size1-1; i++) {
				if(a[i]>=b[i]) {
					continue;
				}
				else {
					flag = 1;
				}
			}
			if(flag == 0) {
				System.out.println("Arrays are Comptible");
			}
			else if(flag == 1) {
				System.out.println("Arrays are Not Compatible");
			}
		}
}	
	




















