public class Find_min_max {
    public static void main(String args[]){
        int array[] = {2,3,1,6,8,5};
        Find_min_max instance = new Find_min_max();
        // instance.maxNum(array);
        // instance.minNum(array);
        System.out.println(instance.minNum(array));
        System.out.println(instance.maxNum(array));
    }

    public int minNum(int[] array){
        int min = array[0];
        for (int i=0;i<array.length;i++){
            if (array[i]<min){
                min = array[i];
            }
        }
        // System.out.println(min);
        return min;
    }

    public int maxNum(int[] array){
        int max = array[0];
        for (int i=0;i<array.length;i++){
            if (array[i]>max){
                max = array[i];
            }
        }
        // System.out.println(max);
        return max;
    }
}
