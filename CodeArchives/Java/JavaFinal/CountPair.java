import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class CountPair {
    public static void main(String[] args) {
        Integer[] array = {2,1,3,2,2,5,7,1,9,5,7,8,9,4,3};
        Set<Integer> set = new HashSet<Integer>();
        for(Integer num : array){
            set.add(num);
        }
        Map<Integer,Integer> dict = new HashMap<>();

        for(Integer num:set){
            Integer count = 0;
            for(Integer rep: array){
                if(num==rep){
                    count+=1;
                }
            }
            dict.put(num, count);
        }

        System.out.println(dict);
    }
}
