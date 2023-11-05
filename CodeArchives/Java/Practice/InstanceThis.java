public class InstanceThis {
    String cvar;

    InstanceThis(String cvar){
        this.cvar = cvar;
        System.out.println(cvar);
    }

    void display(){
        System.out.println(cvar);
    }

    public static void main(String args[]){
        InstanceThis o = new InstanceThis("local variable");
        o.display();
    }
}
