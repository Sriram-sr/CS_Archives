import java.util.Arrays;

public class ArraysDemo {
    int num = 21;
    void arrays(){
        System.out.println(num);
        int[] array = {1,2,3};
        System.out.println(Arrays.toString(array));
    }

    public static void main(String args[]){
        ArraysDemo obj = new ArraysDemo();
        obj.arrays();
    }
}
