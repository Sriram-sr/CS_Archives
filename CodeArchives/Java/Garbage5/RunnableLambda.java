public class RunnableLambda{
    public static void main(String args[]){
        Thread t1 = new Thread(() -> {
                        for(int i=1;i<=5;i++){
                            System.out.println(i*i);
                        }
        });

        Thread t2 = new Thread(() ->{
            for(int i=1;i<=5;i++){
                System.out.println(i*i*i);
            }
        });
        t1.start();
        t2.start();
    }
}