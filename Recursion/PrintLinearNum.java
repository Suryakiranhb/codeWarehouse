import java.util.*;

public class PrintLinearNum {
		public static void rec(int start, int i) {
			if(start == i+1) {
				return;
			}
			else {
				System.out.println(start);
				rec(start+=1, i);
				System.out.println("Backtracking "+(start-1));
			}
			
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter number ");
			int num = sc.nextInt();
			rec(1,num);
			sc.close();
	}
}
