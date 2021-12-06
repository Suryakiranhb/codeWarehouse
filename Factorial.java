import java.util.Scanner;

class Factorial {
	public static void main(String[] args) {
		int fact = 1;
		System.out.println("Do you want a while loop or a for loop? Enter w or f for the same.");
		Scanner sc = new Scanner(System.in);
		char choice = sc.next().charAt(0);
		
		System.out.println("Enter the number you wanna find the factorial of: ");
		int num = sc.nextInt();
		
		if(choice=='f') {
			for (int i=1; i<=num; i++) {
				fact = fact*i;
			}
			System.out.println("The factorial of the number "+num+" using for loop is "+fact);
		}
		else if (choice == 'w') {
				int i = 1;
				while (i<=num) {
					fact=fact*i;
					i++;
				}
				System.out.println("The factorial of the number "+num+" using while loop is "+fact);
				
		}
	}
}