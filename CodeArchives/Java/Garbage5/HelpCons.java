
class Basser{
    String names;

    Basser(String nme){
        names = nme;
        System.out.println("name from basser "+ names);
    }
}

class Mainclass extends Basser{
    int num;
    String name;

    Mainclass(int num,String name){
        this(name);
        this.num  = num;
        this.name = name;
    }

    Mainclass(String name){
        super(name);
        this.name = name;
        System.out.println(name);
    }
}



public class HelpCons {
    public static void main(String args[]){
        Mainclass ref = new Mainclass(22,"Sri");
    }
}
