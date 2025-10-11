import java.io.*;
import java.util.StringTokenizer;
import java.lang.Math;

public class Lifeguards {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("lifeguards.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("lifeguards.out")));

		StringTokenizer st = new StringTokenizer(r.readLine());
		int N = Integer.parseInt(st.nextToken());
        int[] shiftsl=new int[N];
        int[] shiftsr=new int[N];
        for (int i=0; i<N; i++){
            st = new StringTokenizer(r.readLine());
            shiftsl[i]=Integer.parseInt(st.nextToken());
            shiftsr[i]=Integer.parseInt(st.nextToken());
        }

        int[] time=new int[1002];

        for (int i=0; i<N; i++){
            int x=shiftsl[i];
            int y=shiftsr[i];
            for (int j=x; j<y; j++){
                time[j]++;
            }
        }

        int ans=0;

        for (int i=0; i<N; i++){
            int cur_max=0;
            int x0=shiftsl[i];
            int y0=shiftsr[i];
            for (int j=x0; j<y0; j++){
                time[j]--;
            }
            for (int k=0; k<1001; k++){
                if (time[k]>0){
                    cur_max++;
                }
            }
            for (int a=x0; a<y0; a++){
                time[a]++;
            }
            ans=Math.max(ans,cur_max);
        }

        pw.println(ans);
        
        
		pw.close();
        
	}
}
