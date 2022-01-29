package com.practice.surya.messingabout;

import java.util.Scanner;

public class AltSumDifference {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number");
		int num = sc.nextInt();
		int[] a = new int[num];
		System.out.println("Enter values");
		for(int i=0; i<=num-1; i++) {
			a[i] = sc.nextInt();
		}
		int ans = 0;
		for(int i=0; i<=num-1; i++) {
			if(i<(num-1-i)) {
//			System.out.println(a[i]+ " " +a[num-1-i] );
			int temp = a[i] - a[num-i-1];
			temp = Math.abs(temp);
			ans = ans +temp;
			}
			else {
				break;
			}
		}
		System.out.println("The alternate sum difference is: "+ ans);
		sc.close();
	}
}
