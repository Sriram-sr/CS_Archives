public class Fibb_Using_recur {
    static int n1=0,n2=1,n3=0;

    static void recursively_execute(int count){
        if (count>0){
            n3=n1+n2;
            System.out.print(n3+" ");
            n1=n2;
            n2=n3;
            recursively_execute(count-1);
        }
    }

    public static void main(String...args) {
        System.out.print(n1+" "+n2+" ");
        int count = 10;
        recursively_execute(count-2);
    }
}
