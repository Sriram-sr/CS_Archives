package Programs;


class Mainer implements Cloneable{
    int cvar = 2343;
    void display(){
        System.out.println(true);
    }

    public Object clone() throws CloneNotSupportedException{
        return clone();
    }
}
public class StringDemo {
    public static void main(String args[]) throws CloneNotSupportedException{
        Mainer ref = new Mainer();
        Mainer ref2 = (Mainer)ref.clone();
        System.out.println(ref2.cvar);
    }
}
