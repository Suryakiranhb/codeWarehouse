package com.practice.tekstac.strings;

import java.util.Scanner;

public class Regex {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the pan card number"); {
		String pan = sc.nextLine();
		if(pan.matches("[A-Z]{5}[0-9]{4}[A-Z]{1}")) {
			System.out.println("Valid PAN number");
		}
		else {
			System.out.println("Invalid PAN number");
			}
		}
	}
}
