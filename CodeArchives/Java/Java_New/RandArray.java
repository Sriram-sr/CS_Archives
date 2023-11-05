import java.util.Random;
import java.util.Arrays;

public class RandArray {
    public static void main(String args[]){
        int[] array = new int[5];
        Random r = new Random();
        
        for(int i=0;i<array.length;i++){
            array[i] = r.nextInt(10,20);
        }
        System.out.println(Arrays.toString(array));
    }
}
