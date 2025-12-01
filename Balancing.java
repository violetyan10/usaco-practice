import java.io.*;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;
import java.lang.Math;
import java.util.Collections;
import java.util.ArrayList;



public class Balancing {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("balancing.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("balancing.out")));

		StringTokenizer st = new StringTokenizer(r.readLine());
        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int[] cowsl=new int[N];
        int[] cowsr=new int[N];
        for (int i=0; i<N; i++){
            st = new StringTokenizer(r.readLine());
            cowsl[i]=Integer.parseInt(st.nextToken());
            cowsr[i]=Integer.parseInt(st.nextToken());
        }
		int minimum=Integer.MAX_VALUE;
        Set<Integer> As = new HashSet<>();
        Set<Integer> Bs = new HashSet<>();
        for (int i=0; i<N; i++){
            As.add(cowsl[i]+1);
            Bs.add(cowsr[i]+1);
        }
        ArrayList<Integer> AList = new ArrayList(As);
        Collections.sort(AList);
        ArrayList<Integer> BList = new ArrayList(Bs);
        Collections.sort(BList);
        
        for (int a: AList){
            //pw.println(a);
            for (int b: BList){
                //pw.println(b);
                int topL=0;
                int topR=0;
                int botL=0;
                int botR=0;
                for (int c=0;c<N;c++){
                    int x2=cowsl[c];
                    int y2=cowsr[c];
                    if (x2<a && y2>b){
                        topL+=1;
                    }
                    else if (x2>a && y2>b){
                        topR+=1;
                    }
                    else if (x2>a && y2<b){
                        botR+=1;
                    }
                    else{
                        botL+=1;
                    }
                
                
                }
                int M=Math.max(Math.max(topL, topR), Math.max(botL, botR));
                minimum=Math.min(minimum,M);
            }
        }
        pw.println(minimum);
		pw.close();
	}
}
