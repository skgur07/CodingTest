import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long num = scanner.nextLong();
        long sum = 0;

        // 받는 숫자는 n임 나머지가 n보다 커질수 없음 근데 몫은 계속 커짐 몫이 커지는 순간 멈춤

        // 자연수가 있음 나누기 num 을 했을때 %와 /가 같으면 += sum

        //     7    2 = 3 ... 1
        //   i    num  i % num  i / sum
        // 1 % 4 == 0 ... 1

        long q = 0;
        for (long i = 1; i < num; i++) { // q가 num 미만일 때만 진행
            q = i * (num + 1);
            sum += q;
        }


        // N = 3 하면 결국 나머지가 1 또는 2 따라서 몫이 3이 넘어가면 X
        //
        System.out.println(sum);
        scanner.close();
    }
}