public class WithoutLoop {
    public static void main(String args[]) {
        int number = 10;
        useRecursionToPrint(number);
        // System.out.println(number);
    }

    public static int useRecursionToPrint(int number) {
        if (number == 0) {
            return 0;
        }
        System.out.println(number);
        return useRecursionToPrint(number-1);
    }
}