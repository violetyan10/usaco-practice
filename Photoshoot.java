import java.io.*;
import java.util

public class Photoshoot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        int Q = sc.nextInt();

        int[][] updates = new int[Q][3];
        for (int i = 0; i < Q; i++) {
            updates[i][0] = sc.nextInt();
            updates[i][1] = sc.nextInt();
            updates[i][2] = sc.nextInt();
        }

        int[][] board = new int[N][N];
        int[][] sums = new int[N][N]; // sum of KxK square with top at r,c

        int maxval = 0;

        for (int i = 0; i < Q; i++) {
            int r = updates[i][0] - 1; // convert to 0-based
            int c = updates[i][1] - 1;
            int v = updates[i][2];

            int diff = v - board[r][c];
            board[r][c] = v;

            int rowStart = Math.max(r - K + 1, 0);
            int rowEnd = Math.min(r, N - K);
            int colStart = Math.max(c - K + 1, 0);
            int colEnd = Math.min(c, N - K);

            for (int a = rowStart; a <= rowEnd; a++) {
                for (int b = colStart; b <= colEnd; b++) {
                    sums[a][b] += diff;
                    maxval = Math.max(maxval, sums[a][b]);
                }
            }

            System.out.println(maxval);
        }

        sc.close();
    }
}
