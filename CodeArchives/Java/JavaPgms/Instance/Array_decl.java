public class Array_decl {
    public static void main(String args[]){
        int newarray[] = new int[3];
        newarray[0] = 12;
        newarray[1] = 24;
        newarray[2] = 21;
        
        for(int i=0;i<newarray.length;i++){
            System.out.println(newarray[i]);
        }

        System.out.println();

        int diffarray[] = {2,23,4,45,2,1};
        for(int i=0;i<diffarray.length;i++){
            System.out.println(diffarray[i]);
        }
    }
}