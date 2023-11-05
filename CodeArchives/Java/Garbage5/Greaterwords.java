public class Greaterwords {
    static void GreaterwordsChar(String test, int k){
        String[] splitted = test.split(" ");
        int[] wordsLength = new int[splitted.length];

        for(int i=0;i<splitted.length;i++){
            wordsLength[i] = splitted[i].length();
        }

        for(int i=0;i<wordsLength.length;i++){
            if(wordsLength[i]>k){
                System.out.println(splitted[i]);
            }
        }
    }

    public static void main(String args[]){
        String test = "hello geeks for geeks is computer science portal";
        int k = 5;
        GreaterwordsChar(test, k);
    }
}
