import java.io.*;
import java.util.StringTokenizer;

public class Gymnastics {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("gymnastics.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("gymnastics.out")));

		StringTokenizer st = new StringTokenizer(r.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[][]ranks=new int[K][N];
        for (int i=0;i<K;i++){
            st = new StringTokenizer(r.readLine());
            for (int j=0;j<N;j++){
                ranks[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        int pairs=0;

        for (int i=1;i<N+1;i++){
            for (int j=i+1;j<N+1;j++){
                boolean consistent=true;
                if (help(ranks[0],i)>help(ranks[0],j)){
                    for (int[] rank:ranks){
                        if (help(rank,i)<help(rank,j)){
                            consistent=false;
                            break;
                        }
                    }
                    if (consistent){
                        pairs++;
                }
                }
                else{
                    for (int[] rank:ranks){
                        if (help(rank,i)>help(rank,j)){
                            consistent=false;
                            break;
                        }
                    }
                    if (consistent){
                        pairs++;
                    }
                }
            }
        }
		pw.println(pairs);
		pw.close();
	}
    public static int help(int[]array,int thing){
        for (int i=0;i<array.length;i++){
            if (array[i]==thing){
                return i;
            }
        }
        return -1;
    }
}