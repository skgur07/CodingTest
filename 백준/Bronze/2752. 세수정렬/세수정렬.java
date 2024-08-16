
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int[] tmp = {a, b, c};

        int max = tmp[0];
        int min = tmp[0];
        int mid = tmp[0];

        for (int i = 1; i < tmp.length; i++) {
            if (tmp[i] > max) {
                max = tmp[i];
            }
        }
        for (int i = 1; i < tmp.length; i++) {
            if (tmp[i] < min) {
                min = tmp[i];
            }
        }

        for (int i = 1; i < tmp.length; i++) {
            if (mid == max || mid == min) {
                mid = tmp[i];
            }
        }
        System.out.println(min + " " + mid + " " + max);

    }
}
