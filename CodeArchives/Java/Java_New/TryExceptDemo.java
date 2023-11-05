class Base{
    static void execute(){
        try{
        int num = 21, result;
        int[] array = {2,3,4};
        result = array[5];
        System.out.println(result);
        }
        catch (Exception error){
            System.out.println(error);
        }
        finally{
            System.out.println("Whatever happens executed");
        }
        System.out.println("This statement should be printed");
    }
}


public class TryExceptDemo extends Base{
    public static void main(String args[]){
        execute();
    }
}
