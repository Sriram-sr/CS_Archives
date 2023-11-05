class Count{
    static int cvar = 0;
    Count(){
        cvar++;
    }

    void show(){
        System.out.println(cvar);
    }
}

public class StatiAccess{
    public static void main(String[] args){
        Count ref1 = new Count();
        Count ref2 = new Count();
        Count ref3 = new Count();
        Count ref4 = new Count();
        ref4.show();
        
    }
}