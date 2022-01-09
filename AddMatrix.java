package com.practice.methods.gcd;

import java.util.Scanner;

public class AddMatrix {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the length (column and row) of arrays 1 and 2");
		int len1 = sc.nextInt();
		int len2 = sc.nextInt();
		int[][] arr1 = new int[len1][len2];
		int[][] arr2 = new int[len1][len2];

		// input for 1st 2d array
		for(int i=0; i<=len1-1; i++) {
			for(int j=0; j<=len2-1; j++) {
				System.out.println("Enter the 1st array element for dimension " +i+ " at position "+j);
				arr1[i][j] = sc.nextInt();
			}
		}
//input for 2nd 2d array
			for(int i=0; i<=len1-1; i++) {
				for(int j=0; j<=len2-1; j++) {
					System.out.println("Enter the 2nd array element for dimension " +i+ " at position "+j);
					arr2[i][j] = sc.nextInt();
				}
			}
//printing the 1st 2d array
			System.out.println("-------------1ST 2D ARRAY IS AS FOLLOWS-----------");
			for(int i=0; i<=len1-1; i++) {
				for(int j=0; j<=len2-1; j++) {
					System.out.print(arr1[i][j]+" ");
				}
				System.out.println();
			}
//printing the 2nd 2d array
			System.out.println("-------------2ND 2D ARRAY IS AS FOLLOWS-----------");
			for(int i=0; i<=len1-1; i++) {
				for(int j=0; j<=len2-1; j++) {
					System.out.print(arr2[i][j]+" ");
				}
				System.out.println();
			}
			System.out.println();
			
//adding array elements from arr1 and arr2 into arr3
			int[][] arr3 = new int[len1][len2];
		    for(int i=0; i<=len1-1; i++) {
		    	for(int j=0; j<=len2-1; j++) {
		    		arr3[i][j]= arr1[i][j]+arr2[i][j];
		    	}
		    }

//printing the sum of arr1 and arr2 i.e., printing arr3
		    System.out.println("-----------THE SUM OF ARRAY 1 AND 2 WOULD BE:-----------");
		    for(int i=0; i<=len1-1; i++) {
				for(int j=0; j<=len2-1; j++) {
					System.out.print(arr3[i][j]+" ");
				}
				System.out.println();
			}
			System.out.println();
	}
}
