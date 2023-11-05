class Reflector implements Cloneable{
    int cvar = 21;

    void refMethod(){
        System.out.println("This is a reflector method");
    }

    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
}



public class UsingCloneDemo {
    public static void main(String args[])throws CloneNotSupportedException{
        Reflector ref1 = new Reflector();
        Reflector ref2 = (Reflector)ref1.clone();
        ref2.refMethod();
    }
}
