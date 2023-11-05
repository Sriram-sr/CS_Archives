public class string_demo {
    public static void main(String args[]) {
        String txt;
        txt = "Hello world";
        System.out.println("The length of the string is "+ txt.length());  // to find the length of string 
        System.out.println("changed text to uppercase is  " + txt.toUpperCase());
        System.out.println("Changed to lower case " + txt.toLowerCase());
   
        String newLine;
        newLine = "Perform various operations with string";
        int index_of_word = newLine.indexOf("e"); // storing the index of character in a variable
        System.out.println(index_of_word);

        String newVar;
        newVar = " This is to be concatenated with previous string";  // concatenating both strings
        System.out.println(newLine.concat(newVar));
        }
    
}
