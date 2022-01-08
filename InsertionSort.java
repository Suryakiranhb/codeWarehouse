package com.practice.methods.gcd;

import java.util.Scanner;


public class InsertionSort {
	public static void main(String[] args) {
   //array setup		
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number of items:");
	int num=sc.nextInt();
	int[] arr = new int[num];
	
	for(int i=0; i<num; i++) {
		System.out.println("Enter the "+(i+1)+"th element: ");
		arr[i] = sc.nextInt();
	}
	for(int i=0; i<num; i++) {
		System.out.println("The "+(i+1)+"th element before sorting is "+arr[i]);
	}
	System.out.println("---------------Insertion sorting below------------");
	// insertion sort code
	int item;
	int j;
	for(int i=1; i<=num-1; i++) {
		item = arr[i];
		j = i-1;
		while(j>=0 && arr[j]>item) {
			arr[j+1] = arr[j];
			--j;
		}
		arr[j+1] = item;
	}
	// display sorted array
	for(int i=0; i<num; i++) {
		System.out.println("The "+(i+1)+"th element after insertion sort is "+arr[i]);
	}
	
	
}
}
