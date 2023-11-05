public class SumForm {
    public static void main(String... args){
        int a = 5, b = 3, n = 5;
        for(int i=0;i<n;i++){
            int sum = 0;
            int t = i;
            while (t>=0){
                int temp = powerFinder(2, t) * b;
                sum+=temp;
                t--;
            }
            sum+=a;
            System.out.println(sum);
        }
        }
    
        static int powerFinder(int base, int exponent){
            int result = 1;
            for(;exponent!=0;exponent--){
                result*= base;
            }
            return result;
        }
    }

