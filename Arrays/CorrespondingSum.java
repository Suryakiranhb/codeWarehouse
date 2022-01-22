package com.practice.tekstac.arrays;

import java.util.Scanner;

public class CorrespondingSum {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int bigger = 0;
		System.out.println("Enter the size of the first array:");
		int size1 = sc.nextInt();
		if(size1<=0) {
			System.out.println("Invalid array size");
			return;
		}
		int[] a = new int[size1];
		System.out.println("Enter elements for first array:");
		for(int i=0; i<=size1-1; i++) {
			a[i] = sc.nextInt();
		}
		System.out.println("Enter the size of the second array:");
		int size2 = sc.nextInt();
		if(size2<=0) {
			System.out.println("Invalid array size");
			return;
		}
		int[] b = new int[size2];
		System.out.println("Enter elements for second array:");
		for(int i=0; i<=size2-1; i++) {
			b[i] = sc.nextInt();
		}
		if(size1>size2) {
			bigger = size1;
		}
		else {
			bigger = size2;
		}
		int[] c = new int[bigger];
		if(size1==size2) {
			for(int i=0; i<=bigger-1; i++) {
				c[i] = a[i]+b[i];
//				System.out.println(c[i]);
			}			
		}
		if(size1<size2) {
			for(int i=0; i<=size1-1; i++) {
				c[i] = a[i]+b[i];
//				System.out.println(c[i]);
			}
			for(int i=size1; i<=size2-1; i++) {
				c[i] = b[i];
//				System.out.println(c[i]);
			}
		}
		
		if(size2<size1) {
			for(int i=0; i<=size2-1; i++) {
				c[i] = a[i]+b[i];
//				System.out.println(c[i]);
			}
			for(int i=size2; i<=size1-1; i++) {
				c[i] = a[i];
//				System.out.println(c[i]);
			}
		}
		System.out.println("Third array elements are as follows:");
		for(int i=0; i<=bigger-1; i++) {
			System.out.print(c[i]+" ");
		}
	}
}
