package Programs;
import java.util.Comparator;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class ComparatorDemo 
{
    public static void main(String args[])
    {
        List<Integer> list = new  ArrayList<>();
        Comparator<Integer> ref = new ComImp();
        list.add(230);
        list.add(160);
        list.add(730);
        list.add(530);
        list.add(299);
        list.add(123);
        list.add(876);
        Collections.sort(list,ref);

        for(int num:list){
            System.out.println(num);
        }
    }    
}
