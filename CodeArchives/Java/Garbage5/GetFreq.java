import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class GetFreq {
    public static void main(String args[]){
        Integer array[] = {2,3,6,5,1,2,8,3,6,24};
        Collection<Integer> list = new ArrayList<>();
        // ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list, array);
        list.add(299);
        list.remove(299);
        System.out.println(list);
    }
}
