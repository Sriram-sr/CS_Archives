public class RecursionDemo {
    static int recursive(int num){
        int Sum;
        if (num > 0){
            Sum = num + recursive(num-1);
            return Sum;
        }
        else {
            return num;
        }
    }

    public static void main(String args[]){
        System.out.println(recursive(10));
    }
}
