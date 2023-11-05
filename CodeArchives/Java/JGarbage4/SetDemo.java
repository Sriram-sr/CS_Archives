import java.util.HashSet;
import java.util.Set;

public class SetDemo {
    public static void main(String args[]){
        Set<Integer>  set =  new HashSet<>();
        set.add(5);
        set.add(18);
        set.add(5);
        System.out.println(set);
    }
}
