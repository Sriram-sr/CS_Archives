public class BindingDemo {
    public static class superclass{
        void print(){
            System.out.println("This is the method in superclass");
        }
    }

    public static class subclass extends superclass{
        @Override
        void print(){
            System.out.println("This is method of subclass");
        }
    }

    public static void main(String args[]){
        superclass A = new superclass();
        superclass B = new subclass();
        A.print();
        B.print();
    }
}
