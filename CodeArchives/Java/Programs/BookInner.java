package Programs;

class Outer
{
    int out_x = 21;

    void instInner()
    {
        Inner inner = new Inner();
        inner.display();
        Inner.statMethod();
    }

    class Inner
    {
        void display(){
            System.out.println("Inner class");
            System.out.println(out_x);
        }

        static void statMethod(){
            System.out.println("dono who is gonna call");
        }
    }
}

class BookInner{
    public static void main(String args[]){
        Outer outer = new Outer();
        outer.instInner();
    }
}