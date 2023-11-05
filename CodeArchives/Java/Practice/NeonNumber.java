public class NeonNumber {
    static Boolean neonnumber(int number){
        int result=0, rem;
        int safe = number;
        while(number>0){
            rem = number%10;
            result+=rem;
            number/=10;
        }
        int checkneon = result*result;
        if (safe == checkneon){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String... args){
        System.out.println(neonnumber(81));
    }
}
