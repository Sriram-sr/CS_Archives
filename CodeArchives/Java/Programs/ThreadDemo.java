class Single extends Thread{
    public void run() {
        Thread tobj = Thread.currentThread();
        System.out.println("Inside thread: "+tobj.getName());
        for(int i=0;i<=5;i++){
            System.out.println(i);
            try{
            Thread.sleep(1000);
            }
            catch (InterruptedException error){
                System.out.println(error);
            }
        }
    }
}

class Second implements Runnable{
    public void run(){
        System.out.println("In the thread");
    }
}

public class ThreadDemo {
    public static void main (String args[]) throws InterruptedException{
        Single ref = new Single();
        Second obj = new Second();
        Thread t = new Thread(obj);
        ref.start();
        t.start();
        ref.join();
        // t.join();
        System.out.println("ID: " + ref.getId());
        System.out.println("Name: "+ ref.getName());
        // ref.join();
        // System.out.println(ref.isAlive());
        System.out.println("ID: "+t.getId());
        System.out.println("Name: "+ t.getName());
        
    }
}
