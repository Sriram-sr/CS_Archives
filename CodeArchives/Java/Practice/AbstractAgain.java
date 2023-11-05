abstract class AbstractAgain {
    abstract int display();
}

abstract class AbsChild extends AbstractAgain{
    void displaya(){
        System.out.println("Ok");
    }

    public static void main(String args[]){
        // AbsChild ref = new AbsChild();
        // ref.display();
        System.out.println(true);
    }
}
