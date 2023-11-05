import java.util.Collections;
import java.util.Arrays;

public class GetMaxArray {
    public static void main(String args[]){
        // Integer array[] = {77,44,22,73,12};
        String array[] = {"helli", "locak", "meiteri", "gipstuff"};
        // Arrays.sort(array,Collections.reverseOrder());
        Arrays.sort(array);
        Arrays.sort(array, Collections.reverseOrder());
        System.out.println(Arrays.toString(array));

    }
}
