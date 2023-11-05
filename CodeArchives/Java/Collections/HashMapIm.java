package Collections;
import java.util.Set;
import java.util.Map;
import java.util.HashMap;


public class HashMapIm {
    public static void main(String args[]){
        Map<String,Integer> dict = new HashMap<>();
        dict.put("EEE", 97);
        dict.put("M2", 98);
        dict.put("Eng", 91);
        dict.put("Chem", 67);
        Set keyset = dict.keySet();
        
        for(Object key:keyset){
            System.out.println(key+" : "+dict.get(key));
        }

        Set<Map.Entry<String,Integer>> kvpair = dict.entrySet();
        
        for(Map.Entry<String,Integer> kv : kvpair){
            System.out.println(kv.getKey()+kv.getValue());
        }

    }
}
