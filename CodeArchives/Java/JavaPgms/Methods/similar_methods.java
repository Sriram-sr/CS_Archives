package Methods;

public class similar_methods {

    static int addNumbers(int n1,int n2){
        return n1+n2;
    }
  // same methods with similar names overloaded 
     // based on arguments
    static double addNumbers(double n1,double n2){
        return n1+n2;
    }
    public static void main(String args[]){
        System.out.println(addNumbers(3, 9));
        System.out.println(addNumbers(2.35, 5.65));
    }
}
