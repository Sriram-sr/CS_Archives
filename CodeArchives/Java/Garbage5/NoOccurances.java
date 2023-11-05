import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NoOccurances {
    public static void main(String args[]){
        Integer[][] test_list = {{4, 5, 5, 4}, {5, 4, 3}};
        Integer[] result = new Integer[test_list.length];
        ArrayList<Integer[]> list = new ArrayList<>();
        int K = 5, N = 2 ;
        int idx=0;
        for(Integer[] sub:test_list){
            int count = 0;
            for(int i:sub){
                if (i==K){
                    count+=1;
                }
            }
            if (count==N){
                System.out.println(Arrays.toString(sub));
                list.add(sub);
            }
        }
        
        // System.out.println(list.toString(list));
    }
}
