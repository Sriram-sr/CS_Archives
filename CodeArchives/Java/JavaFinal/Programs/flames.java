import java.util.ArrayList;

public class flames{
    static String flamesCalculator(StringBuilder name1, StringBuilder name2){
        ArrayList<String> commonChars = new ArrayList<>();
        for(int i=0;i<name1.length();i++){
            if(name2.toString().contains(Character.toString(name1.charAt(i)))){
                int nameIdx = name2.indexOf(Character.toString(name2.charAt(i)));
                System.out.println(nameIdx);
            }
        }

        // for(int i=0;i<name1.length();i++){
        //     if(name2.toString().contains(Character.toString(name1.charAt(i)))){
        //         commonChars.add(Character.toString(name1.charAt(i)));
        //     }
        // }
        // System.out.println(commonChars);
        // for (String i :commonChars){
        //     int name1_idx = name1.indexOf(i);
        //     name1.replace(name1_idx,name1_idx+1,"");
        //     int name2_idx = name2.indexOf(i);
        //     System.out.println(name2_idx);
        //     name2.replace(name2_idx,name2_idx+1, "");
        //     System.out.println(name2);
        // }
        // int count = name1.length()+name2.length();        
        // StringBuilder flames = new StringBuilder("flames");
        // int start = 0, end = flames.length(), temp =0;
        // while(flames.length()>1){
        //     for(int i=start;i<end;i++){
        //         temp+=1;
        //         if(temp==count){
        //             flames.replace(i, i+1, "");
        //             if (i==flames.length()){
        //                 start = 0;
        //                 end = flames.length();
        //                 temp = 0;
        //                 break;
        //             }
        //             System.out.println(flames);
        //             start = i;
        //             end = flames.length();
        //             temp = 0;
        //             break;
        //         }

        //         if(i==flames.length()-1){
        //             start = 0;
        //             end = flames.length();
        //         }
        //     }
        // }

        return "";
    }
    public static void main(String[] args) {
        StringBuilder name1 = new StringBuilder("veeramanikandan");
        StringBuilder name2 = new StringBuilder("daenerys");
        flamesCalculator(name1, name2);
    }
}