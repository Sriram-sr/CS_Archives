public class checknInsert{
    int[] array;

    public checknInsert(int size){
        array = new int[size];
        for (int i=0;i<array.length;i++){
            array[i] = Integer.MIN_VALUE;
        }
    }

    public void insert(int location,int value){
        try{
            if (array[location]== Integer.MIN_VALUE){
                array[location] = value;
                System.out.println("Inserted");
            }
            else {
                System.out.println("Declined");
            }
        }
        catch (ArrayIndexOutOfBoundsException error) {
            System.out.println(error);
        }
        return;
        
    }
    public static void main(String...args){
        checknInsert instance = new checknInsert(6);
        instance.insert(0, 10);
        instance.insert(1, 10);
        instance.insert(2, 10);
        instance.insert(3, 10);
        instance.insert(2, 10);
        instance.insert(4, 10);
        System.out.println(Integer.MIN_VALUE);
    }
}
