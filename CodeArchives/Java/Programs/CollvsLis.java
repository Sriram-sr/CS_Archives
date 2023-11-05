package Programs;

interface CollectionMimic
{
    void add();
    void sort();
}

interface ListMimic extends CollectionMimic
{
    void addAll();
    void special();
}

class Demo implements ListMimic
{
    public void add(){
        System.out.println("add executed");
    }

    public void sort(){
        System.out.println("Sort executed");
    }

    public void addAll(){
        System.out.println("Add all implemented");
    }

    public void special(){
        System.out.println("splecial Exceuted");
    }
}

public class CollvsLis
{
   public static void main(String args[])
   {
        CollectionMimic collectionRefernce = new Demo();
        ListMimic listReference = new Demo();
        
   }

}
