package CollectionDemo;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class List_Collect {
    static void usingCollectionInterface(){
        Collection<Integer> list = new ArrayList<Integer>();
        list.add(2);
        list.add(22);
        list.add(12);
        for(int i:list){
            System.out.println(i);
        }
        System.out.println(list);
        list.remove(2);
        System.out.println(list);
    }

    static void usingListInterface(){
        List<Integer> list = new ArrayList<Integer>();
        List<Integer> list2 = new ArrayList<Integer>();
        list2.add(155);
        list.add(215);
        list.add(51);
        list.add(1325);
        list.add(2,110);
        list.set(2, 111);
        list.add(155);
        System.out.println(list);
        list.retainAll(list2); //removeAll , addAll methods are there.
        System.out.println(list);

    }

    static void usingOnlyArrayList(){
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(1);
        list.add(3);
        System.out.println(list);
        list.remove(1);
        System.out.println(list);
    }
    public static void main(String args[]){
        usingListInterface();
    }
}
