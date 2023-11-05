class grandfather{
    public void message(){
        System.out.println("Im grandfather");
    }
}

class Father extends grandfather{
    public void newmessage(){
        System.out.println("Im father");
    }
}

class Son extends Father{
    public static void main(String args[]){
        Son instance = new Son();
        instance.newmessage();
        instance.message();
    }
}