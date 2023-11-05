package Programs;
import java.util.Arrays;

class Instanter{
    int cvar = 22;

    Instanter(int cvar){
        this.cvar = cvar;
    }
}
public class ObrefArray {
    public static void main(String args[]){
        Instanter ref1 = new Instanter(12);
        Instanter ref2 = new Instanter(90);
    }
}
