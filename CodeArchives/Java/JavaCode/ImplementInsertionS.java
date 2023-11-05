import java.util.Arrays;

public class ImplementInsertionS{
    public static void main(String[] args) {
        int array[] = {5,4,10,1,6,2};
        int n = array.length;
        
        for(int i=1;i<n;i++){
            int temp = array[i];
            int j = i-1;

            while(j>=0&&array[j]>temp){
                array[j+1] = array[j];
                j--;
            }

            array[j+1] = temp;

        }
        System.out.println(Arrays.toString(array));
    }
}