class Execute{
    void square(){
        for(int i=1;i<=5;i++){
            System.out.println("Square: "+i*i);
        }
    }
}

public class DiffClassThread extends Thread{
    public void run(){
        Execute ref = new Execute();
        ref.square();
    }

    // public void run(){
    //     Execute ref = new Execute();
    //     ref.square();
    // }
    public static void main(String args[]){
        DiffClassThread obj = new DiffClassThread();
        obj.start();
    }
}
