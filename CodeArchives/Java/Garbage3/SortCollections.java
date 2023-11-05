import java.util.Collections;
import java.util.ArrayList;
import java.util.LinkedList;

public class SortCollections {
    public static void main(String args[]){
        ArrayList<String> list = new ArrayList<String>();
        list.add("Hello");
        list.add("World");
        list.add("Python");
        System.out.println(list);
        // list.remove(0);
        // list.set(0,"Kumar");
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);

        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.add(2);
        ll.addFirst(23);
        System.out.println(ll);
    }
}
