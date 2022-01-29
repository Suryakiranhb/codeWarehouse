package com.practice.methods.messingabout;

import java.util.Scanner;

public class FarmFest {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Number of baskets");
		int no = sc.nextInt();
		if(no<=0 || no>10) {
			System.out.println("Invalid number of baskets");
		}
		else {
			int[] a = new int[no];
			System.out.println("Number of mangoes in each basket");
			for (int i=0; i<=a.length-1; i++) {
				a[i] = sc.nextInt();
			}
			int even = 0, odd=0, flag =0;
			for(int i=0; i<=a.length-1; i++) {
				if(a[i]<0) {
					flag = 1;
					break;
				}
				else if(a[i]%2==0) {
					even++;
				}
				else {
					odd++;
				}
			}if(flag == 0) {
			if(odd == 0 && even>=1) {
				System.out.println("Even");
			}
			else if(even == 0 && odd>=1) {
				System.out.println("Odd");
			}
			else {
				System.out.println("Rearrange the mangoes");
			}
			}
			else {
				System.out.println("Invalid Input");
			}
		}
		sc.close();
	}
}
