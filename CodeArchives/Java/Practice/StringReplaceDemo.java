public class StringReplaceDemo {
    public static void main(String[] args){
        String sample = "HelloJava";
        char replace_text = sample.charAt(4);
        sample = sample.replace(replace_text, 'p');
        System.out.println(sample);
    }
}
