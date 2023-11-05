import java.text.DecimalFormat;
import java.util.Arrays;

public class FindMedian{
    static int median(int nums1[], int nums2[]){
         int[] concat_array = new int[nums1.length+nums2.length];
         for(int i=0;i<nums1.length;i++){
            concat_array[i] = nums1[i];
         }
         int last_idx = nums1.length;
         for(int i=0;i<nums2.length;i++){
            concat_array[last_idx] = nums2[i];
            last_idx+=1;
         }
         Arrays.sort(concat_array);
         System.out.println(Arrays.toString(concat_array));

         
         if(concat_array.length % 2 != 0){
            return concat_array[concat_array.length/2];
         }
         else{
            int ret_idx = concat_array.length/2;
            double two_sum = (double)(concat_array[ret_idx-1] + concat_array[ret_idx])/2;
            System.out.println(two_sum*100000);
            // return two_sum;
         }
         return 1;
    }

    public static void main(String[] args) {
        int nums1[] = {1,3};
        int nums2[] = {4,2,5,6};
        System.out.println(median(nums1, nums2));
        DecimalFormat df = new DecimalFormat("#0.####");
        String num = df.format(0.912385);
        System.out.println(num);
        // System.out.println(Integer.parseInt(num));
    }
}