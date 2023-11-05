import java.util.HashSet;

public class HassetDemo {
    public static void main(String args[]){
        HashSet<Integer> hset = new HashSet<Integer>();
        hset.add(2);
        hset.add(90);
        hset.add(23);
        System.out.println(hset);
        hset.remove(223);
        System.out.println(hset);
    }
}
