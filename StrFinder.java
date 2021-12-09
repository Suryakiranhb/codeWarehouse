package com.practice.methods.gcd;

public class StrFinder {
		boolean check(String a, char b) {
			char arr[] = a.toCharArray();
			for(int i=0; i<=a.length(); i++ ) {
				if(arr[i] == b) {
					return true;
				}
			}
			return false;
		}
}
