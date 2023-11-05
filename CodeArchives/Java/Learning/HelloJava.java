import java.math.BigDecimal;

public class HelloJava{
    public static void main(String args[]){
      //  System.out.println(fnum.getClass().getSimpleName());
      Integer randvalue = Integer.MIN_VALUE;
      System.out.println(randvalue);
      Float rand = Float.MAX_VALUE;
      System.out.println(rand);
      BigDecimal number = new BigDecimal("56");
      BigDecimal point = new BigDecimal("0.9");
      System.out.println(number.subtract(point));
      System.out.println(point.add(number));
      char num = 65535;
      System.out.println(num);
}
}

// single line command is this.
/*  This is a document 
  comment in java
  I can type in any number of lines here
 */