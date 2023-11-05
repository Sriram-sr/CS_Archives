import java.util.*;

public class ArrayToList {
    public static void main(String args[]){
        Integer[] array = {5,4,3,8,7,9,0};
        List list = new ArrayList<>(Arrays.asList(array));
        list.add(4);
        System.out.println(list.contains(19));
        System.out.println(list);
    }
}
