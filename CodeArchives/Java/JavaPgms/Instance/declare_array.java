import java.util.Arrays;
public class declare_array{
    public static void main(String args[]){
        int[] array = null;
        array = new int[5];
        array[0] = 12;
        array[1] = 12;
        array[2] = 12;
        array[3] = 12;
        array[4] = 12;
        // array[5] = 12;
        int[] list = {2,3,6,5,9,2};
        System.out.println(Arrays.toString(list));

        System.out.println(array[0]);
        int random = Integer.MAX_VALUE;
        int min = Integer.MIN_VALUE;
        System.out.println("Min: "+ min);
        System.out.println("random: "+random);
    }
}