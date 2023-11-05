class Scratch {

    static int fibonnacci(number) {
        int result = 1;
        while(number>0) {
            result *= number;
            --number;
        }
        return result;
        }
    
    public static void main(String[] args) {
        int number = 5;
        fibonnacci(number);
    }
}