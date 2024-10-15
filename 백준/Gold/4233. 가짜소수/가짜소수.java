import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int p = 0, a = 0;
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            p = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());

            if (p == 0 && a == 0)
                break;

            if (isPrime(p))
                System.out.println("no");
            else if (a == BigInteger.valueOf(a).modPow(BigInteger.valueOf(p), BigInteger.valueOf(p)).intValue())
                System.out.println("yes");
            else
                System.out.println("no");
        }
    }

    public static boolean isPrime(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}
