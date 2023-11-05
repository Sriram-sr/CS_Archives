import java.util.Arrays;
import java.util.ArrayList;

public class RemoveString {
    public static void main(String args[]){
        String str = "Geeksforgeeks";
        String[] temp = str.split("");
        String sample[] = {"a","l","o"};
        String samp = String.join("", sample);
        System.out.println(samp);
        ArrayList strlist = new ArrayList<>(Arrays.asList(temp));
        ArrayList result = new ArrayList<>();
        for(int i=0;i<strlist.size();i++){
            if(! result.contains(strlist.get(i))){
                result.add(strlist.get(i));
            }
        }
        System.out.println(result);
        String res = String.join("",result);
        System.out.println(res);
    }
}
