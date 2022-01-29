package com.practice.methods.messingabout;
//click ---> https://www.hackerrank.com/challenges/bon-appetit/problem for the problem statement

import java.util.Scanner;

public class BillSplit {
	static int split(int[] bill, int k, int b) {
		int count =0;
		for(int i=0; i<=bill.length-1; i++) {
			if(i==k) {
				continue;
			}
			else {				
				count = count + bill[i];
			}
		}
		System.out.println("Brian's total: "+count);
		count = count/2;
//		System.out.println("HALF:"+count);
		if(b>count) {
			int brian_owes = count-b;
			return brian_owes;
		}
		else if(b<count){
			int anna_owes = count-b;
			return anna_owes;
		}
		else return 0;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of items ordered: ");
		int n = sc.nextInt();
		System.out.println("Enter the item Anna didnt eat:");
		int k = sc.nextInt()-1;
		int[] bill = new int[n];
		System.out.println("Enter the cost for each food in bill:");
		for(int i=0; i<=n-1; i++) {
			bill[i] = sc.nextInt();
		}
		int billTotal = 0;
		for (int i = 0; i < bill.length; i++) {
			billTotal = billTotal + bill[i];
		}
		System.out.println("Total bill from both: "+billTotal);
		System.out.println("Enter the amout of money Brian charged Anna for her share of the bill");
		int b = sc.nextInt();
		int res = split(bill, k, b);
		if(res == 0) {
			System.out.println("Bon Appetit!");
		}
		else if(res<0 ){
			System.out.println("Brian gotta pay "+(Math.abs(res))+" back to Anna");
		}
		else if(res>0) {
			System.out.println("Anna gotta pay "+res+" more to Brian");
		}
		sc.close();
	}
}
