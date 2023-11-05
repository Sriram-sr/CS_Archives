class Square extends Thread{
    public void run(){
        for (int i=1;i<=5;i++){
            System.out.println("Square: "+i*i);
            try{ Thread.sleep(500); } catch (Exception e){}        

        }
    }
}

class Cube extends Thread{
    public void run(){
        for (int i=1;i<=5;i++){
            System.out.println("Cube: "+i*i*i);
            try{ Thread.sleep(500); } catch (Exception e){}        
        }
    }
}

public class TwoThreadsDemo {
    public static void main(String args[]){
        Square sq = new Square();
        Cube cu = new Cube();
        sq.start();
        try{ sq.join(); cu.join(); } catch (Exception e){}        
        cu.start();
    }
}
