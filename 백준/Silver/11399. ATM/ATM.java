import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        List<Integer> ls = new ArrayList<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        String [] input = bf.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            ls.add(Integer.valueOf(input[i]));
        }

        Collections.sort(ls);

        int sum = 0, tmp = 0;
        for (int i: ls) {

            sum += i ;
            tmp += sum;


        }
        System.out.println(tmp);



    }
}
