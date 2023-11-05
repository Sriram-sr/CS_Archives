public class SleepDemo {
    public static void main(String args[]){
        for(int i=0;i<5;i++){
            try{ Thread.sleep(1000); } catch (Exception e ){}
            System.out.println("Hello");
            System.out.println(new Thread().isAlive());
        }
    }
}
