class SuperClass{
    int number;
    String text;

    SuperClass(int num, String txt){
        number = num;
        text = txt;
    }

    void display(){
        System.out.println("Name is "+text+" and number is "+number);
    }
}

public class UseSuper extends SuperClass{
    UseSuper(int num, String txt){
        super(num, txt);
    }

    void subdisplay(){
        System.out.println("Super class number is "+number);
    }
    public static void main(String... args){
        // SuperClass ref = new SuperClass(90, "Sriram");
        UseSuper ref = new UseSuper(100, "Varsha");
        ref.display();
        ref.subdisplay();
    }
}
