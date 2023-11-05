public class Classvar {
    int classVar = 33;

    void retreiveCvar(){
        System.out.println(classVar);
    }
    public static void main(String... args){
        // Classvar o = new Classvar();
        // o.retreiveCvar();
        new Classvar().retreiveCvar();
    }
}
