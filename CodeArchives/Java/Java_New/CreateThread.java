class User extends Thread{
    public void run(){
        System.out.println(Thread.currentThread());
        System.out.println(Thread.currentThread().getId());
        for(int i=0;i<5;i++){
            System.out.println(i);
        }
    }

    public void run(int number){
        System.out.println("Hello");
    }
}


public class CreateThread {
    public static void main(String args[]){
        User u = new User();
        u.start();
    }
}
