class Outer{
    void methOne(){
        System.out.println("Method 1");
    }

    void methTwo(){
        System.out.println("Method 2");
    }

    void useMethods(){
        methOne();
        methTwo();
    }
}


public class FuncCalInside {
    public static void main(String args[]){
        String input = System.console().readLine("Write anything .... ");
        System.out.println(input);
    }
}
