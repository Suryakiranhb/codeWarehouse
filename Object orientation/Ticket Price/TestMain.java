package com.practice.tekstac;

import java.util.Scanner;

public class TestMain {
		public static BusTicket getTicketDetails() {
			Scanner sc = new Scanner(System.in);
			BusTicket bt = new BusTicket();
			//person set
			System.out.println("Enter the passenger name:");
			String name = sc.nextLine();
			System.out.println("Enter the gender(M or F / m or f");
			char gender = sc.next().charAt(0);
			System.out.println("Enter the age:");
			int age = sc.nextInt();
			sc.nextLine();
			
			Person p = new Person();
			p.setName(name);
			p.setGender(gender);
			p.setAge(age);
			bt.setPerson(p);
			
			System.out.println("Enter the ticket no:");
			int ticketNo = sc.nextInt();
			bt.setTicketNo(ticketNo);
			sc.nextLine();
			System.out.println("Enter the ticket price:");
			float ticketPrice = sc.nextFloat();
			bt.setTicketPrice(ticketPrice);
			
			return bt;
		}
		public static void main(String[] args) {
			TestMain t1 = new TestMain();
			BusTicket bt1 = new BusTicket();
			
			bt1 = t1.getTicketDetails();
			bt1.calculateTotal();
			System.out.println("Ticket no:"+bt1.getTicketNo());
			bt1.getPerson();
			System.out.println("Price of a ticket :"+bt1.getTicketPrice());
			System.out.println("Total Amount :"+bt1.getTotalAmount());
			
 	}
}
