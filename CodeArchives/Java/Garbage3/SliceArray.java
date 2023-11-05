import java.util.Arrays;

public class SliceArray {
    public static void main(String args[]){
        int[] array = {2,3,4,5,6,7,8,10};
        int[] sliced = Arrays.copyOfRange(array, 1, 4);
        System.out.println(Arrays.toString(sliced));
    }
}
