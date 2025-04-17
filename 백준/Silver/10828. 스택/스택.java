import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        ArrayList<Integer> stack = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String command = sc.nextLine();

            if (command.startsWith("push")) {
                int value = Integer.parseInt(command.split(" ")[1]);
                stack.add(value);
            } else if (command.equals("pop")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.remove(stack.size() - 1));
                }
            } else if (command.equals("size")) {
                System.out.println(stack.size());
            } else if (command.equals("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else if (command.equals("top")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.get(stack.size() - 1));
                }
            }
        }

        sc.close();
    }
}
