import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        Queue<Integer> q = new LinkedList<>();
        int last = -1;

        for (int i = 0; i < n; i++) {
            String[] c = sc.nextLine().split(" ");
            String command = c[0];

            switch (command) {
                case "push":
                    int x = Integer.parseInt(c[1]);
                    q.offer(x);
                    last = x;
                    break;
                case "pop":
                    if (q.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(q.poll());
                    }
                    break;
                case "size":
                    System.out.println(q.size());
                    break;
                case "empty":
                    if (q.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if (q.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(q.peek());
                    }
                    break;
                case "back":
                    if (q.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(last);
                    }
                    break;
            }
        }

        sc.close();
    }
}
