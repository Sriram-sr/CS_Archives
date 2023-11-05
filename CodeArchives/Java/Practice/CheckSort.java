import java.util.Arrays;
import java.util.Collections;

public class CheckSort {
    public static void main(String args[]){
        Integer num = 23;
        int unwrapped = num.intValue();
        System.out.println(unwrapped);
        System.out.println(num);
        Integer numarray[] = {3,9,7,6,1,0,2,13};
        String strarray[] = {"kite", "snake", "Boomer", "Oops"};
        Arrays.sort(numarray);
        System.out.println("Sorted numarray in ascending order is "+Arrays.toString(numarray));
        Arrays.sort(numarray,Collections.reverseOrder());
    }
}
