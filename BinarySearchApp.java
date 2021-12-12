package com.practice.methods.gcd;

import java.util.Arrays;
import java.util.Scanner;

public class BinarySearchApp {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the number of elements");
			int ele = sc.nextInt();
			int[] arr =  new int[ele];
			System.out.println("Enter the elements: ");
			for(int i=0; i<ele; i++) {
					arr[i] = sc.nextInt();
			}
			Arrays.sort(arr);
			System.out.print("The elements, ");
			for(int i=0; i<arr.length; i++) {
				System.out.print(arr[i]);
				System.out.print(" ");
			}
			System.out.println(" are successfully entered and sorted. \nNow, enter the key to search for: ");
			int key = sc.nextInt();
			BinarySearchAlgo search = new BinarySearchAlgo();
			boolean res = search.binarySearch(arr, key);
			if(res==true) {
				System.out.println("The key is present");
			}
			else {
				System.out.println("The key is not present");
			}
		}
}
