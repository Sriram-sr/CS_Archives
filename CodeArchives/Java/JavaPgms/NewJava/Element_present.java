import java.util.Arrays;

public class Element_present {
     public static void main(String agrs[]){
        int[] testarray = {2,3,4,5,6,8};
        boolean retval  = Arrays.asList(testarray).contains(5);
        System.out.println(retval);
     }   
}
