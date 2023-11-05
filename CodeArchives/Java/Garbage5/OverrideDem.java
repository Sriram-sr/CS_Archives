class Robust{
    final void finalMethod(){
        System.out.println("This is a final method");
    }
}

abstract class Weaker extends Robust{
    abstract void show();
}


public class OverrideDem {
    public static void main(String args[]){
        Robust robust = new Robust();
    }
}
