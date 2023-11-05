class Functions{
    static void square(){
        for (int i=1;i<=5;i++){
            System.out.println("Square: "+ i*i);
        }
    }

    static void cube(){
        for(int i=1;i<=5;i++){
            System.out.println("Cube: "+ i*i*i);
        }
    }
}

class Threadclass extends Thread{
    public void run(){
        Functions.cube();
        Functions.square();
    }
}

public class MultiThreadDemo {
    public static void main(String args[]){
        Threadclass thread1 = new Threadclass();
        thread1.start();
    }
}
