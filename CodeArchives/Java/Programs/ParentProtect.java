package Programs;

class Protector
{
    int cvar = 23;
    protected int privateMethod()
    {
        return cvar;
    }
}

class Normaller extends Protector
{
    void useMethod()
    {
        System.out.println(privateMethod());
    }
}

public class ParentProtect {
    public static void main(String args[]){
        Normaller ref = new Normaller();
        ref.useMethod();
    }
}
