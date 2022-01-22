package com.practice.tekstac.arrays;

import java.util.Scanner;

public class ArraySwap {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//first array input
		System.out.println("Enter the number of elements in the first array : ");
		int array1no = sc.nextInt();
		if (array1no < 0) {
			System.out.println("Invalid range");
			return;
		}
		int[] a = new int[array1no];
		System.out.println("Enter the elements in the first array");
		for (int i = 0; i <= array1no - 1; i++) {
			a[i] = sc.nextInt();
		}

//second array input
	System.out.println("Enter the number of elements in the second array : ");
	int array2no = sc.nextInt();
	if(array2no<0)
	{
		System.out.println("Invalid range");
		return;
	}
	int[] b = new int[array2no];
	if(array1no!=array2no)
	{
		System.out.println("Unable to swap. Size differs.");
		return;
	}
	System.out.println("Enter the elements in the second array : ");
	for(int i = 0;i<=array2no-1;i++)
	{
		b[i] = sc.nextInt();
	}
//swapping
	for(int i=0; i<=array1no-1; i++) {
		int temp = a[i];
		a[i] = b[i];
		b[i] = temp;
	}
//printing swapped arrays
	System.out.println("The first array after swapping is : ");
	for(int i=0; i<=array1no-1; i++) {
		System.out.print(a[i]+" ");
	}
	System.out.println();
	System.out.println("The second array after swapping is : ");
	for(int i=0; i<=array2no-1; i++) {
		System.out.print(b[i]+" ");
	}
	}
}
