import java.util.Arrays;

public class AddReverse {
    static void reverseAdd(int[] l1, int[] l2){
        int num, result = 0, result_string_length;
        String num1 = "", num2 = "";
        for(num = l1.length-1;num>=0;num--){
            num1+= String.valueOf(l1[num]);
        }
        for(num=l2.length-1;num>=0;num--){
            num2+=String.valueOf(l2[num]);
        }
        result = Integer.parseInt(num1) + Integer.parseInt(num2);
        String st = String.valueOf(result);
        result_string_length = st.length();
        int[] rev_list = new int[result_string_length];
        for(num=result_string_length-1;num>=0;num--){
            rev_list[num] = st.charAt(num);
            rev_list[num] = Integer.parseInt(Character.toString(st.charAt(num)));
        }
        System.out.println(Arrays.toString(rev_list));
    }
    public static void main(String[] args) {
        int [] l1 = {2,4,3};
        int[] l2 = {5,6,4};
        reverseAdd(l1, l2);
    }
}
