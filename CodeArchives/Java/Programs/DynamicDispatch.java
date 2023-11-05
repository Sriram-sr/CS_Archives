package Programs;

interface CollectionMime{
    void remove(String ele);
}

interface ListMime extends CollectionMime{
    void remove(int idx);
}

class ArListMime implements ListMime{
    public void remove(String ele){
        System.out.println("Implemented method from Collection");
    }

    public void remove(int idx){
        System.out.println("Implemented method from List");
    }
}

public class DynamicDispatch {
    public static void main(String args[]){
        CollectionMime colref = new ArListMime();
        ListMime lisref = new ArListMime();
        colref.remove("STR");
        lisref.remove(21);
    }    
}
