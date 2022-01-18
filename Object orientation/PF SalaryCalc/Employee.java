package com.practice.tekstac;

public class Employee {
	private int employeeId;
	private String employeeName;
	private double salary;
	private double netSalary;
	
	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}
	public void setEmployeeName(String employeeName) {
		this.employeeName = employeeName;
	}
	public void setSalary(double salary) {
		this.salary = salary;
	}
	public void calculateNetSalary(int pfpercentage) {
		double deduction = salary*pfpercentage/100;
		netSalary = salary-deduction;
	//	return netSalary;
	}
	public double getNetSalary() {
		return netSalary;
	}
	public int getEmployeeId() {
		return employeeId;
	}
	public String getEmployeeName() {
		return employeeName;
	}
	public double getSalary() {
		return salary;
	}
}
