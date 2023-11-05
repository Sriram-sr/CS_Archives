public class DifftypeCast {
    static double mymethod(float x, float y){
        return (int)x+y;
    }
    
    public static void main(String args[]){
        System.out.println(mymethod(3.2f, 8.9f));
    }
}
