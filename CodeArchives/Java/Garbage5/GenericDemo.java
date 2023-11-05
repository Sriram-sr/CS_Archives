class Restricted<E>{
    E obj;

    Restricted(E ref){
        obj = ref;
    }

    E getObject(){
        return obj;
    }
}

public class GenericDemo {
    public static void main(String args[]){
        Restricted<Integer> ref = new Restricted<Integer>(15);
        System.out.println(ref.getObject());
        Restricted<String> ref2 = new Restricted<String>("Hello");
        System.out.println(ref2.getObject());
    }
}
