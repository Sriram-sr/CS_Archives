class MainClass{
    void demomethod() throws ArithmeticException{
        System.out.println("This method may throw io exception");
        int num = 23;
        System.out.println(num/0);
    }
}
public class ThrowsDemo {
    public static void main(String args[]){
        MainClass ref = new MainClass();
        try{
        ref.demomethod();
        }
        catch (ArithmeticException error){}
        catch (ArrayIndexOutOfBoundsException error){
            System.out.println(error);
        }
        System.out.println("Done and dusted");
    }
}
