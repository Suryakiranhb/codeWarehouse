package com.practice.surya.messingabout;

import java.util.Scanner;

public class factorialNonRecursion {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of array elements: ");
		int num = sc.nextInt();
		int[] a = new int[num];
		System.out.println("Enter the array elements:");
		for(int i=0; i<=a.length-1; i++) {
			a[i] = sc.nextInt();
		}
		int sumOfFactorized = 0;
		for(int i=0; i<=a.length-1; i++) {
			if(a[i]>0 && a[i]<10) {
				int factorized = factorizer(a[i]);
				sumOfFactorized = sumOfFactorized + factorized;
			}
		}
		System.out.println("The sum of the factors of the single digit numbers in the array is: "+sumOfFactorized);
		sc.close();
	}
	
	
	static int factorizer(int n) {
		int fact = 1;
		for(int i=1; i<=n; i++) {
			fact = fact*i; 
		}
		return fact;
	}
}
