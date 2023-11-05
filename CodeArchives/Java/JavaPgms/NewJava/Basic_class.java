public class Basic_class {
    String class_variable = "Iam a class variable";

    public  static void main(String args[]){
        Basic_class obj = new Basic_class();
        System.out.println(obj.class_variable); // this is how you can create a object and call a class
        obj.class_variable = "I changed the variable text";
        System.out.println(obj.class_variable);
    }
}
