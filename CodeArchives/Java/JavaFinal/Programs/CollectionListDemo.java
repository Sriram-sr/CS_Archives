import java.util.Collection;
import java.util.List;
import java.util.ArrayList;

public class CollectionListDemo {
    public static void main(String[] args) {
        Collection<Integer> colList = new ArrayList<>();
        List<Integer> lisList = new ArrayList<>();
        colList.add(5);
        colList.add(9);
        colList.add(2);

        lisList.add(5);
        lisList.add(9);
        lisList.add(2);

        colList.remove(9);
        lisList.remove(3);
        System.out.println(colList);
        System.out.println(lisList);
    }    
}
