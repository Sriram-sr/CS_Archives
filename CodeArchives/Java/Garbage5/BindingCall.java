public class BindingCall {
    static class Bouter{
        static void print(){
            System.out.println("Bouter class");
        }
    }

    static class Binner extends Bouter{
        static void print(){
            System.out.println("Binner");
        }
    }

    public static void main(String args[]){
        Bouter bo = new Bouter();
        Bouter bi = new Binner();
        bo.print();
        bi.print();
    }
}
