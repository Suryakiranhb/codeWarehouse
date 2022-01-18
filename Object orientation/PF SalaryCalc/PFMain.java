package com.practice.tekstac;

import java.util.Scanner;

public class PFMain {
	public static Employee getEmployeeDetails() {
		Scanner sc = new Scanner(System.in);
		Employee emp = new Employee();
		System.out.println("Enter Id:");
		int id = sc.nextInt();
		emp.setEmployeeId(id);
		System.out.println("Enter Name:");
		String name = sc.next();
		emp.setEmployeeName(name);
		System.out.println("Enter salary:");
		int salary = sc.nextInt();
		emp.setSalary(salary);
		return emp;
	}
	
	public static int getPFPercentage() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter PF percentage:");
		int pfpercentage = sc.nextInt();
		return pfpercentage;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Employee emp1 = new Employee();
		emp1 = PFMain.getEmployeeDetails();
		int pfp = PFMain.getPFPercentage();
		emp1.calculateNetSalary(pfp);
		
		System.out.println("Id : "+emp1.getEmployeeId());
		System.out.println("Name : "+emp1.getEmployeeName());
		System.out.println("Salary : "+emp1.getSalary());
		System.out.println("Net Salary : "+emp1.getNetSalary());
	}
}
