package com.practice.methods.messingabout;

import java.util.Scanner;

public class WhileLoopArray {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of elements");
		int n = sc.nextInt();
		int i=0;
		int[] a = new int[n];
		while ( i<=n-1) {
			a[i] = sc.nextInt();
			i++;
		}
		while(i>0) {
			System.out.print(a[i-1]+" ");
			i--;
		}
		System.out.println(i);
	}
}
