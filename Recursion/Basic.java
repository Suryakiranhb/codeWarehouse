import java.util.*;

public class Basic {
		public static void rec(int i) {
			if (i==10) {
				return;
			}
			else {
				System.out.println("Recursion level: "+(10-i));
				i+=1;
				rec(i);
				//int j=0;
				System.out.println("Backtracking indicator: "+i);
				//j+=1;
			}
			
		}
		public static void main(String[] args) {
			System.out.println("Enter how many times you want to skip the recursion ");
			Scanner sc = new Scanner(System.in);
			int num = sc.nextInt();
			rec(num);
			sc.close();
	}
