class Superclass{
    int superNum = 90;
    void show(){
        System.out.println("Method in superclass");
    }
}

class Subclass extends Superclass{
    void subshow(){
        System.out.println("Method in subclass");
    }

    void accessParentNonStatic(){
        System.out.println("Got it : "+ super.superNum);
    }
}

public class SubSuperDemo {
    public static void main(String args[]){
        Superclass superObj = new Subclass();
        Subclass subObj = new Subclass();
        subObj.accessParentNonStatic();

    }
}
