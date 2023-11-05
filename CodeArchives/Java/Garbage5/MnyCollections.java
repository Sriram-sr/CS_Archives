import java.util.Collection;

interface Onner{
    void add();
}

interface Twoer extends Onner{
    void sub();
    void mul();
}

class Userof implements Twoer{
    public void sub(){
        System.out.println(true);
    }

    public void mul(){
        System.out.println(true);
    }

    public void add(){
        System.out.println(true);
    }
}

public class MnyCollections {
    
}
