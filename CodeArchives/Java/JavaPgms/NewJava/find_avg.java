import java.util.Arrays;
import java.util.*;

public class find_avg{
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter how many days temperature");
        int days = input.nextInt();
        int[] array = new int[days];
        int prompt = 1,average,count = 0;
        for (int i=0;i<days;i++){
            System.out.println("Enter day "+ prompt + ":");
            int day = input.nextInt();
            array[i] = day;
            prompt+=1;
        }
        // System.out.println(Arrays.toString(array));
        var total = 0;
        for (int i:array){
            total+=i;
        }
        average = total/days;
        System.out.println("Average temperature is " + average);
        for (int i:array){
            if (i>average){
                count+=1;
            }
        }
        System.out.println("Days above average is " + count);

    }
}