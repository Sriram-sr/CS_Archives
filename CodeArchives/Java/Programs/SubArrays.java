package Programs;
import java.util.List;
import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;

public class SubArrays {
    public static void main(String args[]){
        int[][] test_list1 = {{1, 2}, {3, 4}, {5, 6}};
        int[][] test_list2 = {{3, 4}, {5, 7}, {1, 2}};
        ArrayList<int[]> list = new ArrayList<>();
    
        for(int[] sub:test_list1)
        {
            int count = 0;
            for(int[] subs:test_list2)
            {
                if(Arrays.equals(sub,subs))
                {
                    count+=1;
                }
            }
            if(count==0)
            {
                list.add(sub);
            }
        }


        for(int[] sub:test_list2)
        {
            int count = 0;
            for(int[] subs:test_list1)
            {
                if(Arrays.equals(sub,subs))
                {
                    count+=1;
                }
            }
            if(count==0)
            {
                list.add(sub);
            }
        }
        for(int i=0;i<list.size();i++)
        {
            System.out.println(Arrays.toString(list.get(i)));
        }

        }
}           
