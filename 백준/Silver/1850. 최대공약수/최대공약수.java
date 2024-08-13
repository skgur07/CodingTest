
import java.util.Scanner;

public class Main {

    static int gcd(long a, long b) {

        while(b != 0) {
            long r = a % b;
            a = b;
            b = r;
    }
        return (int) a;
    }

    public static void main(String[] args) {


        String str = "1";
        StringBuilder sb = new StringBuilder();

        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();

        int gcd = gcd(b, a);
        System.out.println(str.repeat(gcd));

    }
}
