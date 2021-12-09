package com.practice.methods.gcd;

public class Gcdfind {
	int gcdfinder(int num1, int num2)
	{
	while(num2!=0 ) {
		int num3;
		num3=num1%num2;
		num1=num2;
		num2 = num3;
	}
	return num1;
}
}
