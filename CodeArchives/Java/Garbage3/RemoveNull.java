import java.util.ArrayList;
import java.util.HashMap;

public class RemoveNull {
    public static void main(String args[]){
        HashMap<String,Integer> dict = new HashMap<String,Integer>();
        String array[] = {"gfg", "3", "oop", "9"};
        ArrayList<String> keys = new ArrayList<String>();
        ArrayList<Integer> values = new ArrayList<Integer>();
        for(int i=0;i<array.length;i++){
            try{
                var temp = Integer.parseInt(array[i]);
                values.add(temp);
            }
            catch (NumberFormatException e){
                keys.add(array[i]);
            }
        }
        System.out.println(keys);
        System.out.println(values);
        
        for(int i=0;i<keys.size();i++){
            dict.put(keys.get(i),values.get(i));
        }

        System.out.println(dict);
    }
}
