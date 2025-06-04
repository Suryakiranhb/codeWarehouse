package com.practice.methods.messingabout;

import java.util.Scanner;

public class BusToBoard {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the bus number");
		int no = sc.nextInt();
		if(no>0 && no<9999) {
			int flag = 0;
			for(int i=2; i<no; i++) {
				if(no%i==0) {
					System.out.println("Sorry you cannot board this bus");
					flag = 1;
					break;
				}
			}
			if(flag==0) {
				System.out.println("You can board this bus");
			}
		}
		else {
			System.out.println("Invalid bus number");
		}
	}
}
