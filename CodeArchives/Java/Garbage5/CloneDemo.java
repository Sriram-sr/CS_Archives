import java.util.Collection;

class Busyer implements Cloneable{
    int cvar1 = 20;
    int cvar2 = 30;
    void someMeth(){
        System.out.printf("Your class variables are %d and %d",cvar1,cvar2);
        System.out.println();

    }

    public Object clone() throws CloneNotSupportedException{
        // return (Busyer)super.clone();
        return super.clone();
    }
}


public class CloneDemo {
    public static void main(String args[]) throws Exception{
        Busyer obj1 = new Busyer();
        obj1.someMeth();
        Busyer obj2 = obj1;
        obj2.cvar2 = 300;
        obj1.someMeth();
        Busyer obj3 = (Busyer)obj1.clone();
        obj3.someMeth();
    }
}
