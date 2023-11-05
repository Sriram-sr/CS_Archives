class Incrementer
{
    int cvar = 0;

    synchronized void increment()
    {
        cvar++;
    }
}


public class SynchronisedDemo
{
    public static void main(String args[]) throws InterruptedException
    {
    Incrementer ref = new Incrementer();
    
    Thread t1 = new Thread(new Runnable() {
        public void run(){
            for(int i=0;i<1000;i++){
                ref.increment();
            }
        }
    });

    Thread t2 = new Thread(new Runnable() {
        public void run()
        {
            for(int i=0;i<1000;i++){
                ref.increment();
            }
        }
    });

    t1.start();
    t2.start();
    t1.join();
    t2.join();
    System.out.println("The value after increment is "+ref.cvar);
    }    
}
