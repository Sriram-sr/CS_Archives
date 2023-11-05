package Programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class SortReverse {
    public static void main(String args[]){
        Integer[][] test_list = {{4, 1, 6}, {7, 8}, {4, 10, 8}};

        for(int i=0;i<test_list.length;i++){
            Integer[] temp = test_list[i];
            Arrays.sort(temp,Collections.reverseOrder());
            test_list[i] = temp;
        }
        ArrayList<Integer> ar = new ArrayList<>();
        System.out.println(Arrays.deepToString(test_list));
        // for(Integer[] sub:test_list){
        //     System.out.println(Arrays.toString(sub));
        // }
    }

}
