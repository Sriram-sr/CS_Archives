package Collections;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;

public class HashSetdemo {
    public static void main(String args[]){
        Set<Integer> set = new HashSet<>();
        set.add(1);

        Map<String,String> dict = new HashMap<>();
        dict.put("Hello", "Java");
        dict.put("Hel", "Python");
        dict.put("Helo", "Shell");

        Set<String> ks = dict.keySet();
        System.out.println(ks);
        for(String str:ks){
            System.out.println(dict.get(str));
        }
    }
}
