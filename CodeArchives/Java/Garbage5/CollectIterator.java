import java.util.TreeSet;
import java.util.Iterator;

public class CollectIterator {
    public static void main(String args[]){
        TreeSet<Integer> ts = new TreeSet<>();
        ts.add(21);
        ts.add(19);
        ts.add(7);
        ts.add(3);
        ts.add(8);
        Iterator<Integer> it = ts.iterator();
        while(it.hasNext()){
            int temp = it.next();
            if (temp<5){
                System.out.println(true);
                it.remove();
            }
            System.out.println(it.next());
            try{Thread.sleep(500);}catch(Exception e){}
        }
    }    
}
