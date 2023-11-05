public class BasicCal {
    static int amstrong(int num){
        int result = 0;
        int rem,bal,cube;
        while (num>0){
            rem = num%10;
            cube = rem * rem * rem;
            result+=cube;
            num/=10;
        }
        return result;
    }

    public static void main(String... args){
        System.out.println(amstrong(153));
    }
}
