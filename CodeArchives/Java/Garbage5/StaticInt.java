interface BaseInt{
    static void stmeth(){
        System.out.println("This is a static base method");
    }
}

class Usclass implements BaseInt{
    void usmeth(){
        System.out.println("This is use method");
    }

    static{
        System.out.println("taja");
    }
}

public class StaticInt {
    public static void main(String args[]){
        Usclass ref = new Usclass();
        BaseInt.stmeth();
    }
}
