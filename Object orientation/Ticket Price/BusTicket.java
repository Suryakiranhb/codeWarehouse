package com.practice.tekstac;

public class BusTicket {
	private int ticketNo;
	private float ticketPrice;
	private float totalAmount;
	private Person person;
	
	//setters
	public void setTicketNo(int ticketNo) {
		this.ticketNo = ticketNo;
	}
	public void setTicketPrice(float ticketPrice) {
		this.ticketPrice = ticketPrice;
	}
	public void setTotalAmount(float totalAmount) {
		this.totalAmount = totalAmount;
	}
	public void setPerson(Person person) {
		this.person = person;
	}
	
	//getters
	public int getTicketNo() {
		return ticketNo;
	}
	public float getTicketPrice() {
		return ticketPrice;
	}
	public float getTotalAmount() {
		return totalAmount;
	}
	public Person getPerson() {
		System.out.println("Passenger Name:"+person.getName());
		return person;
	}
	
	//calculate total
	public void calculateTotal() {
		int age1 = person.getAge();
		char g = person.getGender();
		float discount = 0;
		if(person.getAge()<16) {
			discount = (ticketPrice*50)/100;
			totalAmount = ticketPrice - discount;
		}
		else if(person.getAge()>=60) {
			discount = (ticketPrice*25)/100;
			totalAmount = ticketPrice - discount;
		}
		else if(age1>=16 && age1<60) {
			if(g=='f' || g=='F') {
				discount = (ticketPrice*10)/100;
				totalAmount = ticketPrice - discount;
			}
			else {
				totalAmount = ticketPrice;
			}
		}
		setTotalAmount(totalAmount);
		//System.out.println("Ticket no:"+ticketNo);
		//System.out.println("Passenger Name:"+person.getName());
		//System.out.println("Price of ticket : "+ticketPrice);
		//System.out.println("Total Amount : "+totalAmount);
	}

}


