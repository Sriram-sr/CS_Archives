class UserThread extends Thread{
    public void run(){
        System.out.println("Thread is running");
        System.out.println(true);
    }
}

public class RunnableDem {
    public static void main(String args[]){
        UserThread ref = new UserThread();
        ref.start();
        // Thread thread1 = new Thread(ref);
        // thread1.start();
    }
}
