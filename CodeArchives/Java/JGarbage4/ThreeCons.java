import java.util.Arrays;

public class ThreeCons {
    static boolean threeCheck(int array[]){
        for(int i=0;i<array.length;i++){
            int[] temp = Arrays.copyOfRange(array,i,i+3);
            int check = temp[0], flag =0;
            for(int num:temp){
                if(num!=check){
                    flag=1;
                }
            }
            if (flag==0){
                return true;
            }
        }
        return false;
    }

    public static void main(String args[]){
    int array[] = {4, 3, 3, 3, 2, 5, 8};
    System.out.println(threeCheck(array));
    }
}
