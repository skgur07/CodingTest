package silver;

import java.util.Scanner;

public class harmonicMean {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 분모 : den
        // 분자 : num

        int n = sc.nextInt();

        int[] arr = new int[n];
        long[] sum = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }


        long all_den = 1;
        for (int i = 0; i < arr.length; i++) {
            all_den *= arr[i];
        }



        long all_num = 0;
        for (int i = 0; i < arr.length; i++) {
            all_num += arr[i];
        }


        long num = 1, tmp = 0;
        for (int i = 0; i < arr.length; i++) {
            sum[i] = all_den / arr[i];
        }

        for (int i = 0; i < arr.length; i++) {
            tmp += sum[i];
        }



        // 여기서 tmp 즉 분자
        long gcd = gcd(tmp, all_den);

        System.out.println(all_den/gcd + "/" + tmp/gcd);

    }

    static long gcd(long a, long b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

}
