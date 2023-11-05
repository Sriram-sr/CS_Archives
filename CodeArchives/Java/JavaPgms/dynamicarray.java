import java.util.Arrays;

public class dynamicarray{
    int[] array;
    int size,count;

    dynamicarray(){
        array = new int[1];
        size = 1;
        count = 0;
    }

    public void addelement(int num){
        if (count==size){
            addsize();
        }
        array[count] = num;
        count+=1;
    }

    public void addsize(){
        int newsize = size*2;
        int[] temp = new int[newsize];
        for (int i=0;i<newsize;i++){
            if (i<array.length){
            temp[i] = array[i];
            }
        }
        array = temp;
        size = newsize;
    }

    public void shrinksize(){
        int temp[] = new int[count];
        for (int i=0;i<count;i++){
            temp[i] = array[i];
        }
        array = temp;
        System.out.println(Arrays.toString(array));
    }

    public void addElementAt(int pos,int num){
        if (size==count){
            addsize();
        }
        int temp[] = new int[size+1];
        for (int i=array.length-1;i>=pos;i--){
            temp[i+1] = array[i];
        }
        for (int i=0;i<=pos;i++){
            temp[i] = array[i];
        }
        temp[pos] = num;
        array = temp;
        System.out.println(Arrays.toString(array));
    }

    public void removeElement(int pos){
        int[] temp = new int[size];
        for (int i=0;i<pos;i++){
            temp[i] = array[i];
        }
        for (int i=size-1;i>pos;i--){
            temp[i-1] = array[i];
        }
        array = temp;
        System.out.println(Arrays.toString(array));
    }

    public static void main(String args[]){
        dynamicarray instance = new dynamicarray();
        instance.addelement(1);
        instance.addelement(2);
        instance.addelement(3);
        instance.addelement(4);
        instance.addelement(5);
        instance.addelement(6);
        instance.addelement(7);
        instance.addelement(8);
        // instance.addelement(9);
        System.out.println(Arrays.toString((instance.array)));
        instance.shrinksize();
        instance.addElementAt(2, 22);
        instance.removeElement(2);
    }
}