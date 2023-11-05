interface User{
    void getName();

}

public class LambdaDemo {
    public static void main(String args[]){
        User ref = () -> {
            System.out.println("abstract method");
        };
        ref.getName();
    }
}
