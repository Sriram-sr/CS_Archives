public class Construct_arg {
    int x;
    Construct_arg(int y){
        System.out.println("The value of x is " + y);
        x = y;
        System.out.println("y is " + x);
    }

    public static void main(String args[]){
        Construct_arg obj = new Construct_arg(9);
       // obj.x = 900;
       // System.out.println("Rendered value is "+ obj.x);
       System.out.println(obj.x);
    }
}
