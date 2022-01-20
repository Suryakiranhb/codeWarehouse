package com.practice.tekstac.arrays;

import java.util.Scanner;

public class CourseSearch {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter no of course:");
		int no = sc.nextInt();
		if(no>20 || no<=0) {
			System.out.println("Invalid Range");
		}
		else {
			String[] a = new String[no];
			System.out.println("Enter course names");
			for(int i=0; i<=no-1; i++) {
				a[i] = sc.next();
			}
			System.out.println("Enter the course to be searched:");
			String key = sc.next();
			for(int i=0; i<=no-1; i++) {
				if(a[i].equals(key)) {
					System.out.println(key+ " course is available");
					System.exit(i);
				}
			}
			System.out.println(key+" course is not available");
		
		}
	}
}