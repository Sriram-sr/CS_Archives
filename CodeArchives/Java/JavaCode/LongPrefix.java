import java.util.Arrays;

public class LongPrefix{
    static String longestPrefixFinder(String[] strings){
        String compare_str = strings[0], result = "";
        int idx, flag, prev = 0;
        // int prev = -1;
        strings = stringListSlicer(strings, 1);
        for(idx=0;idx<compare_str.length();idx++){
            flag = 0;
            for(String str: strings){
                if(str.length()>0){
                    if (idx<str.length()){
                        if (idx!=0){
                            if ((compare_str.charAt(idx)==str.charAt(idx)) && (str.charAt(idx-1)==compare_str.charAt(prev))){
                                flag+=1;
                            }
                        }
                        else{
                            if((compare_str.charAt(idx)==str.charAt(idx))){
                                flag+=1;
                            }
                        }
                        
                    }
                }
                
            }
            if (flag==strings.length){
                prev = idx;
                result+=Character.toString(compare_str.charAt(idx));
            }
        }
        System.out.println(result);
        return "";
    }

    public static String longestCommonPrefix(String[] strs) {
       
        int pos = 0,min = 9999;                 //line 1
        
        for(int i = 0 ; i<strs.length ; ++i){                 //line 2
            if(strs[i].length() < min)   min = strs[i].length();                 //line 3
        }
        System.out.println(min);
        
        for( ;pos<min ; ++pos){                 //line 4
            
            char k = strs[0].charAt(pos);       
            System.out.println(k);          //line 5
            
            for(int i = 0 ; i<strs.length ; ++i){                 //line 6
                if(strs[i].charAt(pos) != k)                 //line 7
                    return strs[i].substring(0,pos);                   //line 8
            }
            
        }
        
        return strs[0].substring(0,pos);                  //line 9
        
    }
    public static void main(String args[]){
        String[] strings = {"flower","fkow"};
        // longestPrefixFinder(strings);
        String result = longestCommonPrefix(strings);
        System.out.println(result);
    }

    static String[] stringListSlicer(String[] array, int idx){
        String temp[] = new String[array.length-1];
        for(int i=idx;i<array.length;i++){
            temp[i-1] = array[i];
        }
        return temp;
    }
}