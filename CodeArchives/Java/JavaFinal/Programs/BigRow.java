import java.util.Scanner;

public class BigRow {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows: ");
        int row = sc.nextInt();
        System.out.println("Enter number of columns: ");
        int col = sc.nextInt();
        int oneCount = 0;
        int sum = 0;
        int mostRow = 0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                System.out.printf("Enter values for row %s: ",i);
                int tempValue = sc.nextInt();
                sum+=tempValue;
            }
            if(sum>oneCount){
                mostRow = i+1;
                oneCount = sum;
            }
            sum=0;
        }
        System.out.println(mostRow);
    }
}
