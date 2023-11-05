public class ThrowIt {
    static void getMeth(int num){
        try{
            if(num<18){
                throw new ArithmeticException("sjasasja");
            }
            System.out.println("Happy");
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void main(String args[]){
        getMeth(22);
    }
}
