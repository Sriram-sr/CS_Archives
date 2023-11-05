import java.util.Arrays;

public class SwapFirstLast {
    public static void main(String[] args){
        int[] array = {3,5,6,9,1,2,0};
        System.out.println(Arrays.toString(swapit(array)));
    }

    static int[] swapit(int[] array){
        int first = array[0];
        int last = array[array.length-1];
        int temp = first;
        first = last;
        last = temp;
        array[0] = first;
        array[array.length-1] = last;
        return array;
    }
}
