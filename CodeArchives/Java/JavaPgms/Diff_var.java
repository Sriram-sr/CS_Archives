public class Diff_var {
    public static void main(String[] args) {
        String name;
        String place;
        long number;  // long data type to store mobile number
        name = "Sriram";
        place = "Chrompet";
        number = 8428259394L;
        System.out.println(name);
        System.out.println(number);
        System.out.println(place);
        final int new_number = 22;   // declaring a variable which is final and cannot be changed
        System.out.println(new_number);
        // new_number = 80;  // overwriting the variable
        System.out.println(new_number);

        int numer = 90;
        float deci = 0.45f;
        boolean tr_val = true;
        String txt = "This is just text";
        char single_char = 'C';

        String firstname = "sri";
        String lastname = "ram";
        String fullname = firstname + lastname;
        System.out.println("Hello "+fullname);
        System.out.println(txt+" "+single_char+" "+numer+deci+" "+tr_val); // printing all variables in single line

        int first_number = 20,second_number = 30;
        System.out.println(first_number+second_number);  // it will add both values

        int x,y,z = 40;
        x = y = z = 80;  // overwriting z value
        System.out.println(x);
        System.out.println(z);
    }
}