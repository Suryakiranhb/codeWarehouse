package com.practice.methods.messingabout;
import java.util.Scanner;

public class LibraryDetailInformation {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the book name:");
		String bName = sc.nextLine();
		String bName2 = bName.replaceAll(" ", "");
		int flag =0;
		if(bName2.length()<=3) {
			System.out.println("Invalid Book name");
			flag = 1;
		}
		if(flag!=1) {
		System.out.println("Enter the author name:");
		String bAuthor = sc.nextLine();
		String bAuthor2 = bAuthor.replaceAll(" ", "");
		if(bAuthor.length()<=6) {
			System.out.println("Invalid Author name");
			flag =1;
			}
		if(flag ==0) {
			System.out.println(bName+" was written by "+bAuthor);
			}		
		}
		sc.close();
	}
}
