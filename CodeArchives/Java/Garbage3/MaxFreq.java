public class MaxFreq {
    public static void main(String args[]){
        String str = "Geeksforgeeks";
        String strArray[] = str.split("");
        int[] countArray = new int[strArray.length];
        for(int i=0;i<str.length();i++){
            int count = getCount(str, str.charAt(i));
            countArray[i] = count;
        }
        int max = countArray[0];
        for(int num: countArray){
            if (num> max){
                max=num;
            }
        }
        
    }

    static int getCount(String str, char val){
        int count = 0;
        for(int let=0;let<str.length();let++){
            if (str.charAt(let)==val){
                count+=1;
            }
        }
        return count;
    }
}
