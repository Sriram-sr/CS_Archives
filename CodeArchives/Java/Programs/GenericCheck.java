package Programs;
import java.util.ArrayList;
import java.util.List;

public class GenericCheck {
    public static void main(String args[]){
        List<Integer> list = new ArrayList<>();
        list.add(21);
        list.add(20);
        int getter = list.get(0);
        System.out.println(((Object)getter).getClass().getName());
        System.out.println(((Object)getter).getClass().getSimpleName());

    }
}
