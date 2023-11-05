class Executor implements Cloneable{
    int cvar = 22;

    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }

    void justShow(){
        System.out.println("The class variable is "+ cvar);
    }
}

public class CloneDemo {
    public static void main(String[] args) throws CloneNotSupportedException {
        Executor ref1 = new Executor();
        ref1.justShow();
        Executor ref2 = (Executor)ref1.clone();
        ref1.cvar = 999;
        ref2.justShow();
        ref2.cvar = 99;
        ref1.justShow();
    }
}
