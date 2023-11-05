public class Rec_stack {
    static void execute_stack(int n){
        if (n<1){
            System.out.println("Reached the end");
        }
        else{
            execute_stack(n-1);
            System.out.println("n value is "+n);
        }
    }

    public static void main(String args[]){
        // execute_stack(5);
        var variable = "Hello Java";
        System.out.println(variable);
    }
}
