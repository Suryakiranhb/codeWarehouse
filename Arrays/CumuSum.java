package com.practice.tekstac.arrays;

import java.util.Scanner;

public class CumuSum {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of elements");
		int num = sc.nextInt();
		if(num<=0) {
			System.out.println("Invalid Range");
			return;
		}
		else {
			int[] a = new int[num];
			System.out.println("Enter the elements");
			for(int i=0; i<=num-1; i++) {
				a[i] = sc.nextInt();
			}
			//System.out.println(a[i]+" ");
			int cumsum = 0;
			for(int i=0; i<=num-1; i++) {
				cumsum = cumsum + a[i];
				System.out.print(cumsum+ " ");
			}
		}
	}
}
