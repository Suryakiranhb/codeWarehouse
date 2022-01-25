package com.practice.tekstac.strings;

public class Login {
	private String userName;
	private String password;
	
	public Login(String userName, String password) {
		this.userName = userName;
		this.password = password;
	}
	
	public boolean validate() {
		if(userName.matches("john") && password.matches("123abc")) {
			return true;
		}
		else {
			return false;
		}
	}
}
