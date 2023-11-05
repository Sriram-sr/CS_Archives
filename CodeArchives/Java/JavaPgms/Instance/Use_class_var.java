public class Base_Class {
    String name = "Sriram";
    int number = 2017;
    String place = "Chennai";
}

public class Use_class_var {
    public static void main(String[] args){
        Base_Class obj = new Base_Class();
        System.out.println("The player is "+obj.name+"His number is "+obj.number+"His place is "+obj.place);
    }
}
