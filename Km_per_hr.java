import java.util.Scanner;

class Km_per_hr {
	public static void main(String[] args) {
		int meters, mins;
		double m_per_s, km, secs;
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the meters: ");
		meters = sc.nextInt();
		
		System.out.println("Enter the  minutes: ");
		mins = sc.nextInt();
		
		secs = mins*60;
		System.out.println("Seconds are: "+secs);
		m_per_s = meters/secs;
		System.out.print(m_per_s+" meters per second");
		km =  m_per_s * 3.6;
		System.out.println(" or " +km+ " kilometers per hour");		
	}
}