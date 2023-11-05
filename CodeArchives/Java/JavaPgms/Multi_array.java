import java.util.Arrays;

public class Multi_array {
    public static void main(String[] args) {
        int[][] multi_array = new int[][] {{1,2,3,4,5},{6,7,8,9,10}};
        // int[][] multi_array = {{1,2,3,4,5},{6,7,8,9,10}};
        // System.out.println(multi_array);
        System.out.println(Arrays.deepToString(multi_array));  // to print a multi dimentional array 
        System.out.println(multi_array[1][3]);

        for(int[] array : multi_array){
            System.out.println(Arrays.toString(array));
            for(int val : array){
                System.out.println(val);
            }
        }
    }
}
