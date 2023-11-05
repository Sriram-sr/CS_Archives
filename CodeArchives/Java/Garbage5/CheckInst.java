interface Helper{
    void show();
}

class Getter implements Helper{
    public void show(){
        System.out.println("resolved");
    }
}

public class CheckInst {
    public static void main(String args[]){
        Getter ref = new Getter();
        System.out.println(ref instanceof Helper);
    }
}
