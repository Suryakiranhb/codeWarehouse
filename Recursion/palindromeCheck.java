import java.util.*;

public class palindromeCheck {
		public static int rec(char[] a, int l, int r) {
			if(l>=r) {
				return 1;
			}
			else if(a[l]!=a[r]) {
				//swap l and r
					return 2;
			}
			else { 
				rec(a, l+1, r-1);
				return 1;
			}
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter string ");
			String st = sc.next();
			char[] a = st.toCharArray();
			int ans = rec(a, 0, a.length-1);
			if(ans==1) {
				System.out.print("yoooo " +st+ " issa palindrome! ");
			}
			else {
				System.out.print("broda u serious? how would "+st+" be a pali man u trippin");
			}
			//for (int i=0; i<=a.length-1; i++) {
			//	System.out.print(a[i]+"");
			//}
	}
}
