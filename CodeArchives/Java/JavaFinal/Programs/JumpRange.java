import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class JumpRange {
    static Integer[] removeEle(Integer[] array, Integer ele){
       List<Integer> arList = new ArrayList<>();
       for(Integer i=0;i<array.length;i++){
        if(array[i]!=ele){
            arList.add(array[i]);
        }
       }
       Integer[] temp = new Integer[arList.size()];
       temp = arList.toArray(temp);
       return temp;
    }

    public static void main(String args[])
    {
        Integer[] array = {10,20,30,40,50,60,70,80,90};

        while(array.length!=0)
        {
            if(array.length==3)
            {
                for(int i=array.length-1;i>=0;i--)
                {
                    System.out.println(array[i]);
                    array = removeEle(array, array[i]);
                    // System.out.println(Arrays.toString(array));
                }
            }
            for(int j=0;j<array.length;j+=2)
            {
                if(j!=0)
                {
                    System.out.println(array[j]);
                    array = removeEle(array, array[j]);
                    // System.out.println(Arrays.toString(array));
                }
            }
        }
    }
    }
