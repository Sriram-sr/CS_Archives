public class returnClassVar {
    private String privar;

    public void getname(){
        System.out.println(privar);
    }

    public void setname(String name){
        privar = name;
    }
    

    public static void main(String args[]){
        returnClassVar obj = new returnClassVar();
        obj.setname("Sr");
        obj.getname();
        returnClassVar newobj = new returnClassVar();
        newobj.setname("Sr");
        newobj.getname();
    }
}
