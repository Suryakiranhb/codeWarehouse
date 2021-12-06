import java.util.Scanner;

class Day {
	public static void main(String[] args) {
		int n;
		Scanner sc = new Scanner(System.in);
		do {
			System.out.print("Enter the number of the day: ");
			n = sc.nextInt();
			switch(n) {
				case 1: System.out.println("Monday"); break;
				case 2: System.out.println("Tuesday"); break;
				case 3: System.out.println("Wednesday"); break;
				case 4: System.out.println("Thursday"); break;
				case 5: System.out.println("Friday"); break;
				case 6: System.out.println("Saturday"); break;
				case 7: System.out.println("Sunday"); break;
				default : System.out.println("This day number is out of bounds. Please enter from 1 to 7");
			}
				}
		while(n>0|| n<8) ;
		}
	}