import java.util.*;

public class Using2ParametersOnly {
		public static void rec(int i,int res) {
			if(i<1) {
				System.out.println("Result is "+res);
				return;
			}
			else {
				System.out.println(i+" (in result variable, we currently have: "+res+")");
				res+=i;
				rec(i-=1, res);
				//System.out.println("Backtracking "+(start+1));
			}
			
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter number ");
			int num = sc.nextInt();
			rec(num,0);
			sc.close();
	}
}
