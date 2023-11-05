public class checknInsert {
    public checknInsert(int sizeOfarray){
    //     int[] array = new int[sizeOfarray];
           int[] array;
           array = new int[sizeOfarray];
           for (int i=0;i<array.length;i++){
            System.out.println(i);
        }
    }

    public void insertfunc(int element,int position){
        
    }
    public static void main(String args[]){
        checknInsert obj = new checknInsert(5);
        obj.insertfunc(12,1);
    }
}
    

