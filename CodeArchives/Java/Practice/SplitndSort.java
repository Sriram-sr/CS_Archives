import java.util.ArrayList;
import java.util.Arrays;

public class SplitndSort {
    public static void main(String args[]){
        ArrayList<String> evenList = new ArrayList<>();
        String text = "This is a python languages";
        String[] array = text.split(" ");
        System.out.println(Arrays.toString(array));
        for(String word : array){
            if (word.length()%2==0){
                evenList.add(word);
            }
        }
        System.out.println(evenList);
    }
}
