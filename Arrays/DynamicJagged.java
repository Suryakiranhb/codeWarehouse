package com.practice.methods.messingabout;

import java.util.Scanner;

public class DynamicJagged {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the array value 1");
		int val = sc.nextInt();
//		System.out.println("Enter the array value 2");
//		int val2 = sc.nextInt();
		int[][] a = new int[val][];
		for(int i=0; i<=val-1; i++) {
			System.out.println("Enter jagged value for level "+i+ " of array");
			int newval = sc.nextInt();
			a[i] = new int[newval];
		}
		System.out.println("Enter values for array");
		for(int i=0; i<=val-1; i++) {
			for(int j=0; j<=a[i].length-1; j++) {
				System.out.println("Enter the value for array dimension "+i+" position "+j);
				a[i][j] = sc.nextInt();
			}
		}
		System.out.println("------------Array values------------");
		for(int i=0; i<=val-1; i++) {
			for(int j=0; j<=a[i].length-1; j++) {
				System.out.print(a[i][j]+" ");
			}
			System.out.println();
		}
	}
}
