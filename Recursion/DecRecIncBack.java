package com.practice.tekstac.strings;
import java.util.*;

public class DecRecIncBack {
		public static void rec(int start, int i) {
			if(start == i) {
				return;
			}
			else {
				System.out.println(start);
				rec(start-=1, i);
				System.out.println("Backtracking "+(start+1));
			}
			
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter number ");
			int num = sc.nextInt();
			rec(num,0);
			sc.close();
	}
}
