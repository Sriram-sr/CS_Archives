import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class RemoveList {
    public static void main(String args[]){
        int[] test_array = {1, 3, 4, 6, 5, 1};
        int item = 1;
        List<Integer> list = new ArrayList<Integer>();
        for(int num:test_array){
            if (num!=item){
                list.add(num);
            }
        }
        System.out.println(list);
    }
}
