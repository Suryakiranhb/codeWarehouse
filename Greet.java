import java.util.Scanner;

public class Greet {
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
		/*	
		 	System.out.println("Hello world! Now in eclipse! Yay!");
			System.out.print("Enter value: ");
			int val = sc.nextInt();
			System.out.println("The value you've entered was: " +val);
			System.out.println("mama naama kim?");
			String name = sc.nextLine();
			System.out.println("Hello " +name);
			System.out.println("Enter char: ");
			char c = sc.next().charAt(0);
			System.out.println(c);
			*/
			
		
			String[] names = new String[5];
			
			for(int i=0; i<5; i++) {
				System.out.println("Enter " +i+ " string: ");
				names[i] = sc.next();
			}
			for (int j = 0; j < names.length; j++) {
				System.out.println(names[j]);
			}
			
			/*
			int arr[] = new int[5];
			for (int i=0; i<5; i++) {
				System.out.println("Enter the " +i+ " number: ");
				arr[i] = sc.nextInt();
			}
			for (int j = 0; j < 5; j++) {
				System.out.println(arr[j]);
			}
			*/
		}
}
