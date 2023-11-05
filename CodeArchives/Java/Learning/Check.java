import java.util.Arrays;
public class Check {
    public static void main(String args[]){
        int[] array = {2,3,4,5,6};
        int[] slice = Arrays.copyOfRange(array,1,array.length);
        System.out.println(Arrays.toString(slice));
        
    }
}
