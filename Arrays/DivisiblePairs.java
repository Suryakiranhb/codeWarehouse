package com.practice.methods.messingabout;

import java.util.Scanner;

public class DivisiblePairs {
		static int divisible(int n, int a[], int k) {
			int count =0;
			for (int i = 0; i < n; i++) {
				for(int j=i+1; j<n; j++) {
					if((a[i]+a[j])%k==0) {
						count++;
					}
				}
			}
			return count;
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter array length:");
			int n = sc.nextInt();
			System.out.println("Enter an integer to divide:");
			int k = sc.nextInt();
			int a[] = new int[n];
			System.out.println("Enter array elements:");
			for (int i = 0; i < a.length; i++) {
				a[i] = sc.nextInt();
			}
			System.out.println(divisible(n,a,k));
		}
	}
