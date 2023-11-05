public class Pyramid_pattern {
    public static void main(String...args){
    int num = 5;
    for(int i=0;i<num;i++){
        for(int j=0;j<num-1-i;j++){
            System.out.print(' ');
        }
        for(int k=0;k<=i;k++){
            System.out.print("* ");
        }
        System.out.println();
    }
// System.out.println("-------------------");

    for(int i=num;i>=0;i--){
        for(int j=num-i;j>0;j--){
            System.out.print(' ');
        }
        for(int k=0;k<i;k++){
            System.out.print("* ");
        }
        System.out.println();
    }
    }
    
}
