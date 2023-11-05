import java.util.ArrayList;

public class forEachLambda {
    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<>();
        al.add(2);
        al.add(1);
        al.add(7);
        al.add(4);
        al.add(5);
        al.add(8);
        
        al.forEach((n) -> {
            if(n%2!=0){
                System.out.println(n);
            }
        });
    }
}
