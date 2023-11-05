public class varargsDemo {
    static void methodOne(boolean truth, int... array){
        System.out.println(array.getClass().getSimpleName());
        System.out.println(array[0]);
    }

     // implementing method overloading with varargs 

    static void methodOne(boolean truth, int num1, int num2, int num3){
        System.out.println("This is a overloaded method");
    }
    
    public static void main(String args[]){
        methodOne(false, 1,2,3);
        int[] array = {4,5,6,78};
        methodOne(true , array);
    }
}
