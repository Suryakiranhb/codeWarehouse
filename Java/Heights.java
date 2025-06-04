import java.util.*;

public class Heights {
	public static void main(String[] args) {
		float[] height = new float[8];
		Scanner sc= new Scanner(System.in);
		for(int i=0; i<=height.length; i++) {
			System.out.println("Enter the height of player "+i);
			height[i] = sc.nextFloat();
		}
		for(int i =0; i<=height.length; i++) {
			System.out.println("The height of player "+i+" is "+height[i]);
		}
	}
}