package com.practice.tekstac.arrays;

public class Student {
	private int id;
	private String name;
	private int[] marks;
	private float average;
	private char grade;
//setters	
	public void setId(int id) {
		this.id = id;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setMarks(int[] marks) {
		this.marks = marks;
	}
	public void setAverage(float average) {
		this.average = average;
	}
	public void setGrade(char grade) {
		this.grade = grade;
	}
//getters]
	public int getId() {
		return id;
	}
	public String getName() {
		return name;
	}
	public int[] getMarks() {
		return marks;
	}
	public float getAverage() {
		return average;
	}
	public char getGrade() {
		return grade;
	}
	
	public void calculateAvg() {
		float total = 0;
		for(int i=0; i<=marks.length-1; i++) {
			total = total+marks[i];
		}
		average = total/marks.length;
	}
	public void findGrade() {
		for(int i=0; i<=marks.length-1; i++) {
			if(marks[i] <=50) {
				grade = 'F';
				return;
			}
			else {
				continue;
			}
		}
		if(average>80 && average<100) {
			grade = 'O';
		}
		else if(average>50 && average<79) {
			grade = 'A';
		}
		else if(average<50) {
			grade = 'F';
		}
		
	}
}










