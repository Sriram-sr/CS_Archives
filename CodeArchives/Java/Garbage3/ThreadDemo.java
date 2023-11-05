class Execute extends Thread{
    public void run(){
        for(int i=1;i<=5;i++){
            System.out.println(i*i);
        }
    }
}

public class ThreadDemo {
    public static void main(String args[]){
        Execute ex = new Execute();
        ex.start();
    }
}
