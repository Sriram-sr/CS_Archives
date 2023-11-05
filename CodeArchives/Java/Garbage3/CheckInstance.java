class Normal{
    void mymeth(){
        System.out.println("Normal method");
    }
}

class User extends Normal{
    void mymeth(){
        System.out.println("User method");
    }
}

public class CheckInstance{
    public static void main(String args[]){
       Normal ref = new User();
    //    ref.mymeth();
    //    User obj = (User)Normal;
    //    obj.mymeth();
    }    
}