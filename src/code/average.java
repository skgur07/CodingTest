package code;

import java.util.Scanner;

public class average {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int max;
        max = arr[0];

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        double all = 0;
        for (int i = 0; i < arr.length; i++) {
            all += (double) arr[i] / max * 100;
        }

        System.out.println((double) all / n);

    }
}
