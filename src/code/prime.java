package code;

import java.util.Scanner;

public class prime {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int a, b, n;

        a = sc.nextInt();
        b = sc.nextInt();
        n = sc.nextInt();

        double c = (double) a / ( double ) b;

        String string_c = Double.toString(c);

        System.out.println(string_c.substring(n+1, n+2));

    }
}
