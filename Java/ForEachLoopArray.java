package com.practice.methods.messingabout;
import java.util.Scanner;

public class ForEachLoopArray {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of elements in array");
		int n = sc.nextInt();
		int[] arr = new int[n];
		for(int x=0; x<=n-1; x++) {
			arr[x] = sc.nextInt();
		}
		int sum =  0;
		for(int y : arr ) {
			// it can be y here or even x here. Doesn't matter. It is the same as using i again and again in different for loops in basic for loop.
			sum = sum+y;
		}
		System.out.println(sum);
	}
}
