public class VarArgs {
    public static void method(int... numberList){
        for(int num:numberList){
            System.out.println(num);
        }
    }

    public static void main(String args[]){
        int numbers[] = {2,10,1,23,6,4,5};
        method(numbers);
    }
}
