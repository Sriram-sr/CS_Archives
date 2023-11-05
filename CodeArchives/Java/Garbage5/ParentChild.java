class Person{
    public void show(){
        System.out.println("Person speaks");
    }
}

class Teacher extends Person{
    public void show(){
        System.out.println("teacher speaks");
    }
}

public class ParentChild {
    public static void main(String args[]){
        Person p = new Person();
        Teacher t = new Teacher();
        p.show();
        t.show();
    }

}
