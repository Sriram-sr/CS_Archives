public class GetSumByRec {
    public static void main(String args[]){
        GetSumByRec obj = new GetSumByRec();
        System.out.println(obj.add_sum(123456));
        System.out.println(obj.easy_sum(123456));
        var power = obj.find_power(2,9);
        System.out.println(power);
        obj.find_binary(123);
    }

    public int add_sum(int num){
        if (num<10){
            return num;
        }
        int mod = num%10;
        int rem = num/10;
        return mod+add_sum((rem));
    }

    public int easy_sum(int num){
        if (num==0){
            return num;
        }
        return num%10+easy_sum(num/10);
    }

    public int find_power(int base,int exp){
        if (exp<1){
            return 1;
        }
        return base*find_power(base, exp-1);
    }

    public void find_binary(int num){
        String bin_str = "";
        while (true){
            int mod = num % 2;
            String str_num = String.valueOf(mod);
            bin_str+=str_num;
            num = num/2;
            if (num==0){
                break;
            }
        }
        String rev_str = "";
        // System.out.println(bin_str);
        for (int i=bin_str.length()-1;i>=0;i--){
            rev_str+=bin_str.charAt(i);
        }
        System.out.println(rev_str);
        System.out.println(bin_str.getClass().getSimpleName());
    }
}
