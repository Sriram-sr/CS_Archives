public class TryCheck {
    public static void main(String args[]){
        try{
            System.out.println(2/0);
        }
        catch (ArithmeticException error){
            // error.printStackTrace();
            System.out.println(error);
        }
    }
}
