public class SwapVar {

    public static void SwapWithoutTemp(int num1,int num2){
        num1 = num1 - num2;
        num2 = num1 + num2;
        num1 = num2 - num1;
        System.out.println("The value of num1 is "+num1+" and num2 is "+num2);
    }
    public static void main(String args[]){
        int m=9, n=5, temp;
        System.out.println("The value of m is "+m);
        System.out.println("The value of n is "+n);
        temp = m;
        m=n;
        n=temp;
        System.out.println("The value of m is "+m);
        System.out.println("The value of n is "+n);
        SwapWithoutTemp(9, 5);
    }
}
