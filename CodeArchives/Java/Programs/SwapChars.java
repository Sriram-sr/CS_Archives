public class SwapChars
{
    public static void main(String args[])
    {
        String inp_str = "14, 625, 498.002";
        String temp = "*";
        inp_str = inp_str.replace(",", temp);
        inp_str = inp_str.replace(".", ",");
        inp_str = inp_str.replace("*", ".");
        System.out.println(inp_str);
    }
}
