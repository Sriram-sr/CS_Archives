import java.util.Arrays;

public class SubCount {
    public static void main(String args[]){
        char common[] =  {'G','E','E','K','S','F','O','R','G','E','E','K'};
        char out = 'G';

        for(int i=0;i<common.length;i++){
            if(common[i]==out){
                continue;
            }
            common[i] = '*';
        }

        System.out.println(Arrays.toString(common));
    }
}
