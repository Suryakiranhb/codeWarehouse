package com.practice.tekstac.arrays;

import java.text.DecimalFormat;
import java.util.Scanner;

public class AverageAge {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter total no. of employees:");
		int total = sc.nextInt();
		if (total < 2) {
			System.out.println("Please enter a valid employee count");
		}
		else {
			System.out.println("Enter the age for  " + total + " employees:");
			int[] a = new int[total];
			int sum = 0;
			int flag = 0;
			for (int i = 0; i <= total - 1; i++) {
				int temp = sc.nextInt();
				if (temp < 28 || temp > 40) {
					System.out.println("Invalid age encountered!");
					flag = 1;
					break;
				}
				else {
					a[i] = temp;
				}
			}
			if (flag == 0) {
				AverageAge age = new AverageAge();
				double ans = age.calculateAverage(a);
				System.out.println("The average age is " + ans);
				DecimalFormat df = new DecimalFormat("####.00");
				System.out.println("More precision o/p: "+df.format(ans));
//		String.format("%.2f",ans);
			}
		}
	}

	double calculateAverage(int[] age) {
		double sum = 0.0;
		for (int i = 0; i <= age.length - 1; i++) {
			sum = sum + age[i];
		}
		double average = sum / age.length;
		return average;
	}
}
