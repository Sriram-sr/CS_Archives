import java.util.HashMap;

class InstanceChecker{
    int cvar;
    InstanceChecker(int cvar){
        this.cvar = cvar;
    }

    public String toString(){
        return "The instance is "+this.cvar;
    }
}
public class QuickCheck{
    public static void main(String[] args) {
        InstanceChecker ref = new InstanceChecker(21);
        System.out.println(ref);
        String s = "leetcode";
        // System.out.println(firstUniqChar(s));
    }

    static String startSplitter(String s, int idx){
        String sub = s.subSequence(0, idx).toString();
        return sub;
    }

    static String endSplitter(String s, int idx){
        String sub = s.subSequence(idx+1, s.length()).toString();
        return sub;
    }

    static int nonRepeat(String s){
        int return_idx  = -1;
        for(int i=0;i<s.length();i++){
            int startflag = -1;
            int endflag = -1; 
            String startSub = startSplitter(s, i);
            String endSub = endSplitter(s, i);
            if(!startSub.contains(Character.toString(s.charAt(i)))){
                startflag = 1;
            }
            if(!endSub.contains(Character.toString(s.charAt(i)))){
                endflag = 1;
            }
            if (startflag == 1 && endflag == 1){
                return i;
            }
        }
        return return_idx;
    }
    
    static int firstUniqChar(String s){
        HashMap<Character, Integer> count = new HashMap<>();
        int n = s.length();
        for(int i=0;i<n;i++){
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0)+1);
        }  

        for(int j=0;j<n;j++){
            if (count.get(s.charAt(index))==1){
                return j;
            }
        }
        return -1;    
    }
}
