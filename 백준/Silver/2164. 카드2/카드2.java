import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            queue.add(i+1);
        }

        while (queue.size() > 1) {
            queue.poll();
            int next = queue.poll();
            queue.add(next);
        }

        System.out.println(queue.poll());

    }
}
