class Outerone{
    int cvar;

    Outerone(int num){
        cvar = num;
    }

    Outerone createObject(){
        Outerone newref = new Outerone(cvar+20);
        return newref;
    }
}



public class CustomObj {
    public static void main(String args[]){
        Outerone ref1 = new Outerone(12);
        Outerone ref2 = ref1.createObject();
        System.out.println(ref1.cvar);
        System.out.println(ref2.cvar);
    }
}
