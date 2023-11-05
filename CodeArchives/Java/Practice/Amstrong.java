public class Amstrong {
    public static void main(String args[]) {
        int number = 371, result = 0;
        String strnum = Integer.toString(number);
        for (int i = 0; i < strnum.length(); i++) {
            char temp = strnum.charAt(i);
            int num = Integer.valueOf(Character.toString(temp));
            result+= num*num*num;
        }
        System.out.println(result);

    }
}
