class Example{
    /* synchronized */ public void display(){
        Thread inside = Thread.currentThread();
        synchronized(this) {
            for(int i=0;i<=5;i++){
            System.out.println(inside.getName());
            System.out.println(i);
            // you can Lock some part of code to synchronised.
            try{
                inside.sleep(500);
            }
            catch(Exception e){}
            }
        }
    }
    }


class Single extends Thread{
    Example reference;
    Single(Example ref){
        reference = ref;        
    }

    public void run(){
        reference.display();
    }
}
public class Thread2Demo {
    public static void main(String args[]) throws InterruptedException{
        Example eobj = new Example();
        Single thread1 = new Single(eobj);
        Single thread2 = new Single(eobj);
        thread2.start();
        thread1.start();
        thread1.join();
    }
}
