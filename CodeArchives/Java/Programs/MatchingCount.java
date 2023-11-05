import java.util.ArrayList;

public class MatchingCount {
    static void loopandFind(String str1, String str2){

        String[] str1_list = str1.split("");
        String[] str2_list = str2.split("");
        ArrayList<String> list = new ArrayList<>();
        ArrayList<String> result = new ArrayList<>();
        for(String i: str1_list){
            list.add(i);
        }
        for (String j: str2_list){
            if (list.contains(j)){
                result.add(j);
            }
        }
        System.out.println(result);
    }    

    public static void main(String args[]){
        String str1 = "abcdef", str2 = "defghia";
        loopandFind(str1,str2);
    }    
        
}
