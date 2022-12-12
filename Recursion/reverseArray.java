public class reverseArray {
		public static void rec(int[] a, int l, int r) {
			if(l>=r) {
				return;
			}
			else {
				//swap l and r
				int temp = a[l];
				a[l] = a[r];
				a[r] = temp;
				rec(a, l+1, r-1);
			}
		}
		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter number ");
			int[] a = {1,23,43,12,34,54,33,2};
			rec(a, 0, a.length-1);
			for (int i=0; i<=a.length-1; i++) {
				System.out.print(a[i]+" ");
			}
	}
}
