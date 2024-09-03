import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        List<Integer> ls = new ArrayList<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        for (int i = 0; i < n; i++) {
            ls.add(Integer.parseInt(bf.readLine()));
        }

        Collections.sort(ls);
        for (int i : ls){
            System.out.println(i);
        }

    }
}
