import java.util.Arrays;

public class Rev_array{
    public static void main(String args[]){
        Rev_array instance = new Rev_array();
        int array[] = {2,1,3,4,0,9,8,5,6};
        instance.reverse_array(array);

    }

    void reverse_array(int array[]){
        for (int i=0;i<array.length/2;i++){
            int last = array.length-1-i;
            int temp = array[i];
            array[i] = array[last];
            array[last] = temp;
        }
        System.out.println(Arrays.toString(array));
    }
}