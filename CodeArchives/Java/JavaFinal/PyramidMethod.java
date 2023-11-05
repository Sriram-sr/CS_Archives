public class PyramidMethod {
    public static void main(String[] args) {
        for(int i=1;i<4;i++){
            for(int k=0;k<3-i;k++){
                System.out.print(" ");
            }
            for(int j=i;j>0;j--){
                System.out.print(j);
            }
            for(int l=2;l<i+1;l++){
                System.out.print(l);
            }
            System.out.println();
        }
    }
}
