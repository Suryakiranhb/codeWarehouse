import java.util.*;

public class FunctionalRecFactorial {
		public static int rec(int i) {
			if(i==0) {
				return 1;
			}
			else {
				return i*rec(i-1);
			}
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter number ");
			int num = sc.nextInt();
			int ans = rec(num);
			sc.close();
			System.out.println(ans);
	}
}
