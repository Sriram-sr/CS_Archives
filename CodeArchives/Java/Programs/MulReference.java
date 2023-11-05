package Programs;


class Newest{
    int cvar =21;

    void show(){
        System.out.println("You can only triger me");
    }

    void trigger(){
        System.out.println("Noting");
    }
}

class Oldest extends Newest{
    int cvar = 20;

    void show(){
        System.out.println("He's variable is "+cvar);
        System.out.println("He's parent's variable is "+super.cvar);
    }

    // void trigger(){
    //     super.show();
    // }
}
public class MulReference {
    public static void main(String argf[]){
        Newest ref = new Oldest();
        ref.trigger();
    }
}
