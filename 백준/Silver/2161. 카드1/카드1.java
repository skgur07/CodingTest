import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {

        Deque<Integer> dq = new ArrayDeque<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            dq.add(i);
        }

        int tmp = 0;
        for (int i = 1; i <= N-1; i++) {
            tmp = dq.getFirst();
            dq.removeFirst();
            dq.addLast(dq.getFirst());
            dq.removeFirst();
            System.out.print(tmp + " ");
        }

        System.out.println(dq.getFirst());


    }
}
