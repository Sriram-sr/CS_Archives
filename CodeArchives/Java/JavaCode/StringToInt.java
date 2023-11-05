import java.sql.Struct;

public class StringToInt {
    static void convertToint(String S){
        String temp = "";
        int idx;
        for(idx=0;idx<S.length();idx++){
            if (Character.isDigit(S.charAt(idx))){
                System.out.println(S.charAt(idx));
                temp+=Character.toString(S.charAt(idx));
            }
            else if(Character.isLetter(S.charAt(idx))){
                System.out.println(idx);
            }
        }
        System.out.println(temp);
    }

    public static void main(String[] args) {
        String s = "   -42";
        convertToint(s);
    }
}
