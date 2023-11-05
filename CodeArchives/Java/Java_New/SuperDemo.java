class SuperClass{
    int supernumber = 90;
    int Number;
    String value;
    SuperClass(int Number, String value){
        this.Number = Number;
        this.value = value;
    }

    SuperClass(){
        System.out.println("Some one initiaed super class");
    }

    void supermethod(){
        System.out.println("Super method");
    }
}

class UserClass extends SuperClass{
    UserClass(int dummy, int Number, String value){
        super(Number, value);
        System.out.println("Some one initiated userclass");
    }

    void usermethod(){
        System.out.println("User method");
        // System.out.println(super.supernumber);
        System.out.println(supernumber);
        super.supermethod();
        System.out.println(Number);
        System.out.println(value);
    }
}

public class SuperDemo{
    public static void main(String args[]){
        UserClass ref = new UserClass(2,3,"Sr");
        ref.usermethod();
    }
}
