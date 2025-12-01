import java.io.*;
import java.util.StringTokenizer;
import java.lang.Math;

public class Triangles {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("triangles.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("triangles.out")));
        StringTokenizer st = new StringTokenizer(r.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] left=new int[N];
        int[] right=new int[N];
        for (int i=0; i<N; i++){
            st = new StringTokenizer(r.readLine());
            left[i]=Integer.parseInt(st.nextToken());
            right[i]=Integer.parseInt(st.nextToken());
        }
        int max_area = 0;
        for (int i=0; i<N; i++){
            int x=left[i];
            int y=right[i];
            int max_x=0;
            int max_y=0;
            for (int j=0; j<N; j++){
                int x_val=left[j];
                int y_val=right[j];
                if (x_val!=x || y_val!=y){
                    if (x==x_val){
                        max_y = Math.max(max_y,Math.abs(y_val-y));
                    }
                    if (y==y_val){
                        max_x = Math.max(max_x,Math.abs(x_val-x));
                    }
                }
            }
            max_area = Math.max(max_area,max_x*max_y);
        }

		pw.println(max_area);

		pw.close();
	}
}
