import java.util.ArrayList;
import java.util.Collection;
import java.util.Vector;

public class IteratorDemo {
    public static void main(String args[]){
        Collection<Integer> list = new ArrayList<Integer>();
        list.add(2);
        list.add(4);
        list.add(8);
        Iterator ot = list.iterator();

        while(ot.hasNext()){
            System.out.println(ot.next());
        }

    }
}