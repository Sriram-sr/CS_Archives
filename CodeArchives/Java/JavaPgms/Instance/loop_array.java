import java.util.Arrays;
public class loop_array{
    public void temp_method(){
        int[] list = {2,3,8,7,1,6,10};
        for (int i:list){
            System.out.print(i+" ");
            
        }
        int[] array = new int[5];
        System.out.println(Arrays.toString(array));
    }

    public static void evaluate(int[] array,int idx){
        if (array==null && idx < 0){
            System.out.println("Not permitted");
        }
    } 
    public static void main(String args[]){
        int[] array = null;
        int idx = -5;
        evaluate(array,idx);
    }
}