package com.practice.tekstac.arrays;

import java.util.Scanner;

public class PandFCount {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter student name ");
		String name = sc.nextLine();
		System.out.println("Enter the no of subjects");
		int subjects = sc.nextInt();
		if(subjects<1 || subjects>20) {
			System.out.println("Invalid input range");
			System.exit(subjects);
		}
		else {
			int[] a = new int[subjects];
			int pass = 0;
			int fail = 0;
			for(int i=0; i<=subjects-1; i++) {
				a[i] = sc.nextInt();
			}
			for(int i=0; i<=subjects-1; i++) {
				if(a[i]<35) {
					fail++;
				}
				else if(a[i]>50) {
					pass++;
				}
			}
			System.out.println(name+" has passed in "+pass+"  subjects and failed in "+fail+" subjects");
		}
	}
}
