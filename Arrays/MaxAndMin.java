package com.practice.tekstac.arrays;

import java.util.Scanner;

public class MaxAndMin {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("How many numbers?");
		int num = sc.nextInt();
		int[] a = new int[num];
		System.out.println("Enter the numbers");
		for(int i=0; i<=num-1; i++) {
			a[i] = sc.nextInt();
		}
		int highest = a[0];
		int lowest = a[0];
		for(int i=1; i<=num-1; i++) {
			if(a[i]>highest) {
				highest = a[i];
			}
			if(a[i]<lowest) {
				lowest = a[i];
			}
		}
		System.out.println("Highest number is "+highest);
		System.out.println("The lowest number is "+lowest);
		
	}
}
