public class Main{
    final int number = 5;
}

class Second{
    static void main(String...args){
        Main instance = new Main();
        // instance.number = 5;
        System.out.println(number);
    }
}