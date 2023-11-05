public class UsethisDemo
{
    int cvar;
    int coVar;

    UsethisDemo(int cvar,int coVar)
    {
        this(coVar);
        this.cvar = cvar;
    }

    UsethisDemo(int coVar)
    {
        this.coVar = coVar;
        System.out.println("Second constructor called successfully");
    }

    int displayVar()
    {
        return cvar;
    }

    public static void main(String args[])
    {
        UsethisDemo ref = new UsethisDemo(99,101);1
        System.out.println(ref.displayVar());
    }
}