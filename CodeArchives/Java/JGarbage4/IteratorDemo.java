// package CollectionDemo;
import java.util.ArrayList;
import java.util.Iterator;

public class IteratorDemo {
    public static void main(String args[]){
        ArrayList<Integer> list = new ArrayList<Integer>();
        Iterator<Integer> it = list.iterator();
        // Iterator<Integer> it = list.listIterator();
        list.add(4);
        list.add(2);
        list.add(1);
        list.add(9);
        list.add(8);
        while (it.hasNext()){
            System.out.println(it.next());
        }
        System.out.println(list);
    }
}
