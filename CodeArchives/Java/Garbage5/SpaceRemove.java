public class SpaceRemove {
    public static void main(String args[]){
        String test_list[] = {"gfg", "   ", " ", "is", "      ", "best"};
        for (String str:test_list){
            int flag = 0;
            for(int i=0;i<str.length();i++){
                if(!Character.isLetter(str.charAt(i))){
                    flag = 1;
                    break;
                }
            }
            if (flag==0){
                System.out.println(str);
            }
        }
    }
}
