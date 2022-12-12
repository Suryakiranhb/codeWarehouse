import java.util.*;

public class recursiveFibonacci {
		public static int rec(int fibo) {
			if(fibo<=1) {
				return fibo;
			}
			else {
				int last = rec(fibo-1);
				int slast = rec(fibo-2);
				return last+slast;
			}
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("fibonacci of? ");
			int n = sc.nextInt();
			int ans = rec(n);
			System.out.println("Fibonacci of "+n+" is "+ans);
	}
}
