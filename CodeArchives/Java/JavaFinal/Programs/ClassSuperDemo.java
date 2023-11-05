class BaseUser
{
    int baseVar1;
    int baseVar2;

    BaseUser(int childVar1,int childVar2)
    {
        baseVar1 = childVar1;
        baseVar2 = childVar2;
        System.out.println("Received from child class");
    }
}

class ChildUser extends BaseUser
{
    ChildUser(int childVar1,int childVar2)
    {
        super(childVar1,childVar2);
    }
}


public class ClassSuperDemo {
    public static void main(String args[]){
        ChildUser ref = new ChildUser(12, 39);
    }
}
