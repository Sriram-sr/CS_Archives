class Super{
    void justprintclass(){
        System.out.println("This is method of super class");
    }
}

public class SubclassDemo extends Super {
    void justprintclass(){
        System.out.println("This is sub class ");
    }

    public static void main(String args[]){
        new SubclassDemo().justprintclass();
}
}