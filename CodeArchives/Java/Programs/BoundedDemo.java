package Programs;

class GenericBounder<T extends Number>{
    T member;

    GenericBounder(T number){
        member = number;
    }

    void giveIt(){
        System.out.println(member);
    }
}

public class BoundedDemo {
    public static void main(String args[]){
        GenericBounder<Integer> ref = new GenericBounder<>(2009);
        ref.giveIt();
    }
}
