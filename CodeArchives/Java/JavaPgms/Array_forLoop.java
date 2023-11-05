public class Array_forLoop {
    public static void main(String args[]) {
        String[] cars = {"Bmw","Audi","Volvo"};
        System.out.println(cars.length);  // to find length of array
        for(String car : cars){
            // System.out.println(car);
            if (car == "Audi"){
                continue;    
            }
            System.out.println(car);
        }
    }
    }
