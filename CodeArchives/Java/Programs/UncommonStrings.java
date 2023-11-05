package Programs;
import java.util.ArrayList;

public class UncommonStrings {
    public static void main(String srga[]){
        String A = "Geeks for Geeks" ;
        String B = "Learning from Geeks for Geeks";
        String[] splittedB = B.split(" ");
        ArrayList<String> al = new ArrayList<>();
        for(String word: splittedB){
            if(!A.contains(word)){
               System.out.println(word);
            }
        }
    }
}
