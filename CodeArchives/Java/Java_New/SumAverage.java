public class SumAverage {
    static void sumandavg(int[] array){
        int sum = 0, avg;
        int length = array.length;
        for (int num: array){
            sum+=num;
        }
        avg = sum/length;
        System.out.println("Sum is "+sum);
        System.out.println("avg is "+avg);
    }

    public static void main(String args[]){
        int array[] = {2,3,4,5,6,};
        sumandavg(array);
    }
}
