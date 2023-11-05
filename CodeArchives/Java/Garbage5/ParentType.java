class Parent{
    int cvar = 9;
    void pmeth(){
        System.out.println(cvar);
    }
}

class Child extends Parent{
    void sunn(){
        System.out.println(false);
    }
}


public class ParentType {
    public static void main(String args[]){
        Parent pobj1 = new Child();
        Parent pobj2 = pobj1;
        pobj1.pmeth();
        pobj1.cvar = 23;
        pobj2.pmeth();
    }    
}
