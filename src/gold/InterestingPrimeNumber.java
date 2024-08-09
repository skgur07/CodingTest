package gold;

import java.util.*;

public class InterestingPrimeNumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int ten_postion, next_postion;

        Integer[] a = new Integer[n];

        ten_postion = (int)Math.pow(10, n-1);
        next_postion = (int)Math.pow(10, n);


        System.out.println(ten_postion);
        System.out.println(next_postion);


        // i <- 1000
        //
        for (int i = ten_postion; i < next_postion; i++) {

            for (int j = 0; j < a.length; j++) {
                a[j] = i % 10;
                i /= 10;
                System.out.println(i);
            }
        }


            System.out.println(Arrays.toString(a));

            List<Integer> list = Arrays.asList(a);
            Collections.reverse(list);
            Integer[] reva = list.toArray(a);

            System.out.println(Arrays.toString(reva));




    }
    static int isPrime(int n) { // 수소면 1 아니면 0
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return 0;
            }
        }
        return 1;
    }
}
