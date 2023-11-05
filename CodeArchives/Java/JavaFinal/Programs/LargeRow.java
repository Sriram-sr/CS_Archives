import java.util.Map;
import java.util.Arrays;
import java.util.HashMap;

public class LargeRow
{
    static int[] removeFirst(int[] array)
    {
        int temp[] = new int[array.length-1];
        for(int i=1;i<array.length;i++)
        {
            temp[i-1] = array[i];
        }
        return temp;
    }
    
    public static void main(String[] args) {
        Map<Integer,Integer> mapDict = new HashMap<>();
        int array[] = {1,1, 0, 1, 0, 0, 0, 0 ,1, 0, 0, 0};
        int row = 4, col = 3;
        Integer[][] rowArray = new Integer[row][col];
        int rowIdx = 0;
        while(row>0){
            Integer[] temp = new Integer[col];
            int idx = 0;
            for(int i=0;i<col;i++)
            {
                temp[idx] = array[0];
                idx+=1;
                array = removeFirst(array);
            }
            rowArray[rowIdx] = temp;
            rowIdx+=1;
            row-=1;
        }

        int idx = 0, compareCount = 0;
        row = 4;
        col = 3;
        for(int i=0;i<row;i++){
            int count = 0;
            for(int j=0;j<col;j++){
                if (rowArray[i][j]==1){
                    count+=1;
                }
            }
            if (count>compareCount){
                idx = i+1;
            }
            compareCount = count;
        }

        System.out.println(idx);
        // System.out.println(Arrays.deepToString(rowArray));
        // for(int i=0;i<rowArray.length;i++){
        //     int count = 0;
        //     for(Integer num:rowArray[i]){
        //         if(num==1){
        //             count+=1;
        //         }
        //     }
        //     mapDict.put(i+1, count);
        // }

        // int rowCount = 0;
        // int resRow = 0;

        // for (Integer key:mapDict.keySet()){
        //     int temp = mapDict.get(key);
        //     if (temp>rowCount){
        //         resRow = key;
        //     }
        //     rowCount = temp;
        // }

        // System.out.println(resRow);
        
    }
}
