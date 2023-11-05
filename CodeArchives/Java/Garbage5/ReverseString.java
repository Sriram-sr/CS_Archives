import java.util.Arrays;

public class ReverseString {
    public static void main(String args[]){
        String[] test_list = {"geeks", "for", "geeks", "is", "best"};
        String result[] = new String[test_list.length];
        
        for(int p=0;p<test_list.length;p++){         
            String temp="";
            for(int i=test_list[p].length()-1;i>=0;i--){
                temp+=test_list[p].charAt(i);
            }
            System.out.println(temp);
         }
    }
}

