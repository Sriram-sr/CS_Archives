class Protecter{
    protected String prMeth(){
        return "Protected";
    }
}

class Normal extends Protecter{
    String  myMeth(){
        return super.prMeth();
    }

    <E> void  randMeth(E[] array){
        for(E ele:array){
            System.out.println(ele);
        }
    }
}


public class ReturnProtected {
    public static void main(String[] args){
        System.out.println(new Normal().myMeth());
        Integer[] array = {2,3,4};
        new Normal().randMeth(array);
    }
}
