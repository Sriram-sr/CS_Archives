class Out{
    int cvar;

    static class In{
        int ivar;
    }
}

public class Innnerclass {
    public static void main(String[] args) {
        Out.In ref = new Out.In();
        
    }
}
