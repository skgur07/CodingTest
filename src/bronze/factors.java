package bronze;

import java.util.Scanner;

public class factors {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        if ( n == 1 ) {
            int tmp = arr[0] * arr[0];
            System.out.println(tmp);
            System.exit(0);
        }

        int min = arr[0];
        int max = arr[0];

        for (int i = 0 ; i < arr.length - 1 ; i++) {
            if (arr[i+1] < min) {
                min = arr[i+1];
            }
        }

        for (int i = 0; i < arr.length - 1 ; i++) {
            if (max < arr[i+1]) {
                max = arr[i+1];
            }
        }

        System.out.println(min * max);

    }
}
