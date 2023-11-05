public class UseObject {
    void methOne(){
        System.out.println("method one");
    }

    void methTwo(UseObject ref){
        ref.methOne();
    }

    public static void main(String args[]){
        UseObject ref = new UseObject();
        ref.methTwo(ref);
    }
}
