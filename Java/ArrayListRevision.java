import java.util.*;

public class ArrayListRevision {
	public static void main(String[] args) {
		List<Integer> a= new  ArrayList<Integer>();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter what u want to append to arraylist ");
		Integer temp = sc.nextInt();
		a.add(temp);
		System.out.println(a);
		System.out.println("Enter the number of elements you want to add to the arraylist now ");
		int g = sc.nextInt();
		for(int i=0; i<=g-1; i++) {
			System.out.println("The "+i+" th element you want to add is : ");
			a.add(sc.nextInt());
		}
		System.out.println(a);
		System.out.println("Which element do you want to remove? ");
		a.remove(Integer.valueOf(sc.nextInt()));
		System.out.println(a);
		System.out.println("Enter the element you want to remove by the index: ");
		a.remove(sc.nextInt());
		System.out.println(a);
		sc.close();
	} 
}
