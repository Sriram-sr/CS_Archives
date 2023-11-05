import java.util.HashMap;

public class HashmapDemo {
    public static void main(String args[]){
        HashMap<String,String> hmap = new HashMap<String,String>();
        hmap.put("Name", "Sriram");
        hmap.put("Age","22");
        hmap.put("Place","Chennai");
        System.out.println(hmap);
        String val = hmap.get("Age");
        System.out.println(val);
        for(String key:hmap.keySet()){
            System.out.println(key);
        }

        for(String value : hmap.values()){
            System.out.println(value);
        }

        for(String kv : hmap.keySet()){
            System.out.println(kv+" : "+hmap.get(kv));
        }
    }
}
