import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayToList {
    public static void main(String args[]){
        String array[] = {"This", "is", "going"};
        List<String> arraylist = new ArrayList<>(Arrays.asList(array));
        arraylist.add("Hello");
        System.out.println(arraylist.contains("Hello"));
        System.out.println(arraylist);
    }
}
