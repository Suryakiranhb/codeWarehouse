import java.util.Scanner;

class Test {
	public static void main(String[] args) {
		int num;
		Scanner sc = new Scanner(System.in);
		do {
			System.out.println("Enter a number");
			num = sc.nextInt();
			System.out.println(num);
		}
		while(num>5);
		sc.close();
	}
}