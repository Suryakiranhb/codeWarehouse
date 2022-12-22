import java.util.*;

public class pyramid {
	
	public static void printer(int n) {
		for(int row=1; row<=n; row++){ //initialized 5 rows,
            int space = n-row;						//space will be 4 so next for loop will go til 4
            for(int col = 1; col<=space; col++){
                System.out.print(" ");
            }
            for(int col=1; col<= (2*row)-1; col++){
            	System.out.print("*");
            }
            System.out.println();
        }
		//-----------------------------------------------------------------
		/*for(int i=1; i<=n; i++) {
            int space = n-i;
            for(int j=0; j<space; j++) {
                System.out.print(" ");
            }
            for(int k=1; k<=(2*i)-1; k++ ) {
                System.out.print("*");
            }
            System.out.println();
        }*/
		//-----------------------------------------------------------------
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the n");
		int d = sc.nextInt();
		printer(d);
	}
}


//n values 1 2 3 4 5 
//(n*2)-1 values 1 3 5 7 9
