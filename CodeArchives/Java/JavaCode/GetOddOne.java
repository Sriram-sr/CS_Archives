import java.util.Map;
import java.util.HashMap;

public class GetOddOne {
    static char getOddone(char[] colors_list){
        int count, idx, nxt;
        Map<Character, Integer> color_map = new HashMap<>();
        for(idx=0;idx<colors_list.length-1;idx++){
            count = 1;
            for(nxt=idx+1;nxt<colors_list.length;nxt++){
                if(colors_list[idx]==colors_list[nxt]){
                    count+=1;
                }
            }
            if(!color_map.containsKey(colors_list[idx])){
                color_map.put(colors_list[idx], count);
            }
        }
        
        for(Map.Entry entry: color_map.entrySet()){
            // if(entry.getValue()%2!=0){
            //     return entry.getKey();
            // }
            System.out.println(entry.getValue()+2);
        }
        
        return 'z';
    }

    public static void main(String args[]){
        char[] colors_list =  {'r','g','b','b','g','y','y'};
        getOddone(colors_list);
    }
}
