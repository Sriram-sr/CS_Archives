class GenericClass<T>{
    T member;

    GenericClass(T member){
        this.member = member;
    }

    T showMember(){
        return member; 
    }
}



public class UseGeneric {
    public static void main(String args[]){
        GenericClass<Character> ref = new GenericClass<>('a');
        System.out.println(ref.showMember());
    }
}
