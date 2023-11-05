class Demonstrator
{
    int cvar;
    String svar;

    Demonstrator(int i, String s){
        this.cvar = i;
        this.svar = s;
    }

    Demonstrator(Demonstrator ref)
    {
        this.cvar = ref.cvar;
        this.svar = ref.svar;
    }

    void display()
    {
        System.out.println("The current objects's cvar and svar is "+this.cvar +" "+ this.svar);
    }
}


public class CpyConst {
    public static void main(String[] args) {
        Demonstrator ref = new Demonstrator(34,"Sublime");
        Demonstrator ref2 = new Demonstrator(ref);
        ref2.svar = "Changed";
        ref2.display();
        ref.display();
    }
}
