package com.practice.tekstac.arrays;

import java.util.Scanner;

public class MultiDimensional {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter no of semesters: ");
		int no = sc.nextInt();
		int[][] a = new int[no][];
		for(int i=0; i<=no-1; i++) {
			System.out.println("Enter no of subjects in "+(i+1)+" semester");
			int subjects = sc.nextInt();
			a[i] = new int[subjects];
		}
		for(int i=0; i<=no-1; i++) {
			for(int j=0; j<=a[i].length-1; j++) {
				System.out.println("Enter marks obtained in semester "+(i+1)+ " for subject "+(j+1));
				int marks = sc.nextInt();
				if(marks<0 || marks>100) {
					System.out.println("You have entered invalid mark.");
					return;
				}
				a[i][j] = marks;
			}
		}
		int maximum = 0;
		for(int i=0; i<=no-1;i++) {
			maximum = a[i][0];
			for(int j=0; j<=a[i].length-1; j++) {
				if(a[i][j]>maximum) {
					maximum = a[i][j];
				}
			}
			System.out.println("Maximum mark in semester "+(i+1)+" is "+maximum);
		}
		}
	}
