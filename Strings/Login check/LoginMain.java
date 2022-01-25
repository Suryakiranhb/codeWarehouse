package com.practice.tekstac.strings;

import java.util.Scanner;

public class LoginMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the username:");
		String username = sc.next();
		System.out.println("Enter the password:");
		String password = sc.next();
		Login l = new Login(username, password);
		boolean result = l.validate();
		if(result == true) {
			System.out.println("Valid user");
		}
		else {
			System.out.println("Invalid user");
		}
	}
}
