class Checker{
    int cvar = 34;
    static int svar = 55;

    void accessAny(){
        System.out.println(cvar + svar);
    }

}


public class CommonVar {
    public static void main(String args[]){
        Checker ref = new Checker();
        ref.accessAny();
    }
}
