class Replayer
{
    public void printMessage(){
        System.out.println("Printed");
    }
}

class CreateMessage extends Thread{
    String message;
    Replayer reference;
    CreateMessage(String message,Replayer reference)
    {
        this.message = message;
        this.reference = reference;
    }

    public void run(){
        synchronized(reference){
            reference.printMessage();
        }
    }    
}


public class SingletonnDemo {
    public static void main(String args[]){
        Replayer ref = new Replayer();
        CreateMessage t1 = new CreateMessage("Hello", ref);
        t1.start();
    }
}
