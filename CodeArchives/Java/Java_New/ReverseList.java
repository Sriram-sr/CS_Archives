import java.util.Collections;
import java.util.Arrays;

public class ReverseList {

    static String usingLogic(int[] array){
        int arlength = array.length;
        int[] newarray = new int[arlength];
        int idx = 0;
        for(int i=arlength-1;i>=0;i--){
            newarray[idx] = array[i];
            idx+=1;
        }
        return Arrays.toString(newarray);
    }

    static void usingCollections(Integer[] array){
        Collections.reverse(Arrays.asList(array));
        System.out.println(Arrays.asList(array));
    }

    public static void main(String args[]){
        int[] array = {4,3,5,6,1,3,7};
        Integer sarray[] = {4,3,5,6,1,3,7};
        System.out.println(usingLogic(array));
        usingCollections(sarray);
    }
}
