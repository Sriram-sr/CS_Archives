import java.util.Arrays;

public class ImplementBubbleS {
    public static void main(String[] args) {
        int[] array = {4,2,5,6,9,11};
        int len = array.length;
        int iter = 1;
        for(int i=0;i<len-1;i++){
            System.out.println("Iteration "+iter);
            iter+=1;
            int flag = 0;
            for(int j=0;j<len-i-1;j++){
                if(array[j]>array[j+1]){
                    flag = 1;
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
            if(flag!=1){
                break;
            }
        }
        System.out.println(Arrays.toString(array));
    }
}
