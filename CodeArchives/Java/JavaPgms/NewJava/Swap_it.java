import java.util.Arrays;

public class Swap_it{
    public static void main(String args[]){
        int[] nums = {1,2,4,6};
        int[][] operations = {{1,3},{4,7},{6,1}};
        for (int sub=0;sub<operations.length;sub++){
            int[] sub_array = operations[sub];
            System.out.println(Arrays.toString(sub_array));
            System.out.println(sub_array[0]);
            boolean check = Arrays.asList(nums).contains(sub_array[0]);
            System.out.println(check);
        }
    }

}