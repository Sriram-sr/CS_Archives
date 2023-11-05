public class Person {
    private String name;
 
    // Getter
    String getName() {
      return name;
    }
 
    // Setter
    void setName(String newName) {
      this.name = newName;
    }

    public static void main(String args[]){
      System.out.println("nothing");
      Person obj = new Person();
      obj.setName("Sriiiiiii");
      System.out.println(obj.getName());
    }
 }
 