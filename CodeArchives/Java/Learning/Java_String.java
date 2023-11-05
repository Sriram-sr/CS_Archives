public class Java_String {
    public static void main(String...args){
        String txt = "Hello world";
        System.out.println(txt.length());
        System.out.println(txt.toUpperCase());
        System.out.println(txt.toLowerCase());
        System.out.println(txt.indexOf("e"));
        System.out.println(txt.charAt(10));

        //to print the unicode(Ascii) value 
        System.out.println(txt.codePointAt(8));
        System.out.println(txt.codePointCount(0,10));

        String string = "Hello World";
        String newstr = string.concat(txt);
        System.out.println(newstr);
        System.out.println(string.compareTo(txt));
    }
}
