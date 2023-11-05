class Threader extends Thread{
    public void run(){
    for(int i=1;i<=5;i++){
        System.out.println("Square: "+ i*i);
    }

    }
}

class Threader2 extends Thread{
    public void run(){
        for(int i=1;i<=5;i++){
            System.out.println("Cube: "+ i*i*i);
        }
    }
}


public class CreateThread {
    public static void main(String args[]){
        Threader t1 = new Threader();
        Threader2 t2 = new Threader2();
        t1.start();
        t2.start();

        Runnable ref = () -> {
            System.out.println("Thread using runable is runing");
        };

        Thread t3 = new Thread(ref);
        t3.start();
    }
}
