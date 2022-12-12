import java.util.*;

public class PrintString {
		public static void rec(int start, String s, int i) {
			if(start == i) {
				return;
			}
			else {
				System.out.println(s);
				rec(start+=1, s, i);
			}
			
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter the string you want to print: ");
			String str = sc.next();
			System.out.println("Enter how many times do you want to print the name? ");
			int num = sc.nextInt();
			rec(0,str,num);
			sc.close();
	}
}
