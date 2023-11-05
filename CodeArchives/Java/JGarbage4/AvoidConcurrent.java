import java.util.ArrayList;
import java.util.Collection;

public class AvoidConcurrent {
    public static void main(String args[]){
        Collection<Integer> list = new ArrayList<Integer>();
        list.add(2);
        list.add(12);
        list.add(3);
        list.add(31);
        for(int element:list){
            if (element==12){
                list.remove(element);
            }
        }
    }


}
