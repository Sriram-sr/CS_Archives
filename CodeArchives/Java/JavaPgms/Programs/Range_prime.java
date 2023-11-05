public class Range_prime {
    public static void main(String args[]) {
        int start = 1;
        int end = 20;
        for(int i=start;i<=end;i++){
            if (i>2){
                int flag = 0;
                for(int j=2;j<i;j++){
                    if(i%j==0){
                        flag = 1;
                        break;
                    }
                }
                if (flag==0){
                    System.out.println(i);
                }
            }
        }
    }
}