public class CreateConstructors {
    String name, breed, color;
    int age;

    CreateConstructors(String name, String breed, String color, int age){
        this(name, breed, color);
        System.out.println("assisteing ine");
    }

    CreateConstructors(String name, String breed, String c){
        this.name = name;
        this.breed = breed;
        this.color = c;
        System.out.println("Copied constructor");
        use();
    }

    public void use(){
        System.out.println("Name is "+name);
    }
    public static void main(String args[]){
        CreateConstructors ref = new CreateConstructors("Sweety", "lab", "blue", 2);
    }
}
