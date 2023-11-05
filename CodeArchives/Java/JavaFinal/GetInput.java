class Mobile{
    void switchOn(){
        System.out.println("Switched on parent");
    }

    void display(){
        System.out.println("Displayed parent");
    }
}

class SmartPhone extends Mobile{
    void switchOn(){
        System.out.println("Switch on child");
    }
    
    void childMethod(){
        System.out.println("Pure child method");
    }
}



public class GetInput{
    public static void main(String args[]){
        SmartPhone ref1 = new Mobile();
    }
}