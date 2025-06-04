import java.util.Scanner;

class LinearSearch {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter array length");
		int n = scan.nextInt();
		int arr[] = new int[n];
		
		System.out.println("Enter array contents: ");
		for (int i = 0; i<=arr.length-1; i++) {
			System.out.println("Enter an element: ");
			arr[i] = scan.nextInt();
		}
		
		System.out.println("Enter the key to search");
		int key = scan.nextInt();
		for (int i=0; i<=arr.length-1; i++) {
			if (key == arr[i]) {
				System.out.println("Key found at index "+i);
				System.exit(0);
			}
		}
		System.out.println("Key not found");
	}
}