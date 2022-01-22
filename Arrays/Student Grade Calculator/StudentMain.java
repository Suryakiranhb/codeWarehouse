package com.practice.tekstac.arrays;

import java.util.Scanner;

public class StudentMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Student s = new Student();
		System.out.println("Enter the id");
		s.setId(sc.nextInt());
		System.out.println("Enter the name");
		s.setName(sc.next());
		System.out.println("Enter the number of subjects"); 
		int subno = sc.nextInt();
		int[] sub = new int[subno];
		for(int i=0; i<=subno-1; i++) {
			System.out.println("Enter marks for subject "+(i+1)+": ");
			sub[i] = sc.nextInt();
		}
		s.setMarks(sub);
		s.calculateAvg();
		s.findGrade();
		
		System.out.println("Id: "+s.getId());
		System.out.println("Name: "+s.getName());
		System.out.println("Average: "+s.getAverage());
		System.out.println("Grade: "+s.getGrade());
		
		sc.close();
	}
}







