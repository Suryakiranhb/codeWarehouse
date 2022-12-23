import java.util.*;

public class reversePyramid {
	
	public static void printTriangle(int n) {
		for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                System.out.print(" ");
            }
            for(int j=((n-i)*2)-1; j>0 ; j--){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
	
	public static void main(String[] args) {
		System.out.print("Enter n: ");
    Scanner sc = new Scanner(System.in);
    int pyramid = sc.nextInt();
    printTriangle(pyramid);
	}
}
