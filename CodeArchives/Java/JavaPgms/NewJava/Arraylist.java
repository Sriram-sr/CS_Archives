import java.util.ArrayList;
import java.util.Arrays;

public class Arraylist {
    public static void main(String args[]){
        ArrayList list = new ArrayList();
        list.add(2);
        list.add(5);
        list.add(7);
        list.add(1);
        var value = list.get(2);
        // System.out.println(value.getClass().getSimpleName());
        System.out.println(list + " " + value);

    }
}
