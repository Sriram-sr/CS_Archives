import java.util.Arrays;

public class first_prob {
    public static void main(String... args){
        int N = 21, max = -1, idx = 0, finMax = -1;
        int Arr[] = {642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642};
        for(int num : Arr){
            if(num>max){
                max = num;
            }
        }
        int tempArray[] = new int[N-1];
        for(int num: Arr){
            if (num!=max){
                tempArray[idx] = num;
                idx+=1;
            }
        }
        System.out.println(Arrays.toString(tempArray));
        for(int num : tempArray){
            if (num>finMax){
                finMax = num;
            }
        }
        System.out.println(finMax);
    }
}