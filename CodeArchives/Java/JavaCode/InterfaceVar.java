import java.util.Scanner;
import java.util.Arrays;
// Remember that the class name should be "Main" and should be "public".
class Main {
	void anonym(){
		Scanner in = new Scanner(System.in);

		// Read the number of test casese.		s
		int T = in.nextInt();
		while (T-- > 0) {
			// Read the numbers a and b.
			int a = in.nextInt();
			int b = in.nextInt();
			
			// Compute the sum of a and b.
			int ans = a + b;
			System.out.println(ans);
		}
	}
	

	static int[] selection_sort(int[] A){
		int i, j, min, temp, n=A.length;
		for(i=0;i<n-1;i++){
			min = i;
			for(j=i+1;j<n;j++){
				if (A[j] < A[min]){
					min = j;
				}
			}
			if(min!=i){
				temp = A[i];
				A[i] = A[min];
				A[min] = temp;
			}
		}
		return A;
	}
	public static void main(String[] args) {
		int[] A = {5,2,8,9,1,3};
		System.out.println(Arrays.toString(selection_sort(A)));
    }
}

	
