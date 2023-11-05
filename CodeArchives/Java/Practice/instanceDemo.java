public class instanceDemo {
    int[] array = {2,3,4};

    void initializeArray(int list[]){
        array = list;
    }

    void printArray(){
        System.out.println(array[0]);
        System.out.println(array[1]);
    }

    public static void main(String args[]){
        instanceDemo instance = new instanceDemo();
        instanceDemo obj = new instanceDemo();
        int[] passinglist = {2,3,4,5,6};
        instance.initializeArray(passinglist);
        obj.printArray();
    }
}
