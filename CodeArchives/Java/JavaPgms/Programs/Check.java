public class Check{
    public static void main(String args[]){
        int n1 = 0;
        int n2 = 1;
        int nth;
        for(int i=0;i<=10;i++){
            System.out.print(n1+" ");
            nth = n1+n2;
            n1 = n2;
            // nth = n1+n2;
            n2 = nth;
        } 


        
    }
}