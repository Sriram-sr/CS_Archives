public class MethodOverloadDemo {
    static int Addelements(int x, int y){
        return x+y;
    }

    static float Addelements(float x, float y){
        return x+y;
    }

    static String Addelements(String x, String y){
        return x+y;
    }

    public static void main(String args[]){
        int addSum = Addelements(2, 3);
        float floatSum = Addelements(2.34f, 1.23f);
        String strout = Addelements(" Hello", " World");
        System.out.println("The sum of int is "+ addSum + " sum of float is " + floatSum + " String output is " + strout);
    }
}
