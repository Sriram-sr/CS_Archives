import java.utils.Arrays;

public class Get_zero_out {
    public static void main(String...args){
        int array[][] = {{1,1,1,},{1,0,1},{1,1,1}};
        int row,col;
        // System.out.println(java.util.Arrays.toString(array));
        for(int i=0;i<array.length;i++){
            for(int j=0;j<(array[i]).length;j++){
                if (array[i][j] == 0){
                    System.out.println(true);
                    row = i;
                    col = j;
                }
            }
        }
        // System.out.println(row);
        // System.out.println(col);

    }
}

