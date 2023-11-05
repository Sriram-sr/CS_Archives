class BB{
    BB(String one){
        System.out.println(one);
    }
}

class AA extends BB{
    AA(String two){
        super(two);
        System.out.println(two);
    }
}



public class BaseChild {
    public static void main(String args[]){
        AA ref = new AA("oneee");
    }
}
