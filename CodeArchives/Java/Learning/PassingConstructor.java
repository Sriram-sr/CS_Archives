public class PassingConstructor {
    String name;
    int num;
    static int change = 3306;

    PassingConstructor(String name,int num){
        this.name = name;
        this.num = num;
        change = num;
        callByConstructor();
    }

    static void callByConstructor(){
        System.out.println("Im called when creating a constructor");
    }

    PassingConstructor(PassingConstructor instance){
        this.name = instance.name;
        this.num = instance.num;
    }

    void display(){
        System.out.println("The student name is "+name+" student number is "+num);
        System.out.println("Let's see static "+change);
    }

    public static void main(String args[]){
        PassingConstructor student1 = new PassingConstructor("Sriram", 333);
        PassingConstructor student2 = new PassingConstructor("Ajay",444);
        PassingConstructor student3 = new PassingConstructor(student2);
        student3.display();
        student2.display();
        student1.display();
    }
}
