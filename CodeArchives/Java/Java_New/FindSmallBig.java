public class FindSmallBig {
    public static int maxNumber(int array[]){
        int max = array[0];
        for(int number : array){
            if(number>max){
                max = number;
            }
        }
        return max;
    }

    public static int minNumber(int[] array){
        int min = array[0];
        for(int number : array){
            if(number<min){
                min = number;
            }
        }
        return min;
    }

    public static void main(String args[]){
        int[] array = {4,3,2,1,9,6,9,-2,8,-7,};
        System.out.println(maxNumber(array));
        System.out.println(minNumber(array));
    }
}
