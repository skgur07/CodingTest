import java.util.Scanner;


public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int b1 = sc.nextInt();
        int m1 = sc.nextInt();

        int b2 = sc.nextInt();
        int m2 = sc.nextInt();

        int x = lcm(m1, m2);

        // 35

        int y = b1 * ( x / m1 ) + b2 * ( x / m2 );

        //2 7 * 5
        //3 5 * 7

        int gcd = gcd(x, y);
        
        System.out.println(y / gcd + " " + x / gcd);

    }

    static int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }

    static int gcd(int a, int b) {
        if ( b == 0 )
            return a;
        return gcd(b, a % b);
    }
}
