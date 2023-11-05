
interface nos{
    void todo();
}

class mysh implements nos{
    public void todo(){
        System.out.println("Implemented interface");
    }
}

class Loook extends mysh{
    public void todo(){
        System.out.println("Inside class");
    }
}
public class ClassHighPrec {
    public static void main(String[] args) {
         Loook l = new Loook();
         l.todo();
    }
    
}
