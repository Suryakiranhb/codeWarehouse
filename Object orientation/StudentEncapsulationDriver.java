package com.practice.methods.encapsulation;

import java.util.Scanner;

public class StudentEncapsulationDriver {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StudentEncapsulation se = new StudentEncapsulation();
		//setting
		System.out.println("Enter the name you wanna store: ");
		String name = sc.next();
		se.setName(name);
		System.out.println("Enter the age: ");
		int age = sc.nextInt();
		se.setAge(age);
		System.out.println("Enter the roll numnber");
		int roll = sc.nextInt();
		se.setRoll(roll);
		//getting
		System.out.println("The name of the student is "+se.getName());
		System.out.println("The age of the student is "+se.getAge());
		System.out.println("The roll number of the student is "+se.getRoll());
	}
}
