// Source: https://usaco.guide/general/io

import java.io.*;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;

public class Bovine {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("cownomics.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cownomics.out")));

		StringTokenizer st = new StringTokenizer(r.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
        String[] spotty = new String[N];
        String[] plain = new String[N];
        for (int i=0;i<N;i++){
            spotty[i]=r.readLine();
        }
        for (int i=0;i<N;i++){
            plain[i]=r.readLine();
        }
		int potential=0;

        for (int i=0;i<M;i++){
            Set<Character> spotty_gen = new HashSet<>();
            for (int s=0;s<N;s++){
                String temp=spotty[s];
                spotty_gen.add(temp.charAt(i));
            }
            Set<Character> plain_gen = new HashSet<>();
            for (int p=0;p<N;p++){
                String temp=plain[p];
                plain_gen.add(temp.charAt(i));
            }
            Set<Character> tempSet = new HashSet<>(spotty_gen);
            tempSet.retainAll(plain_gen);
            if (tempSet.size()==0){
                potential++;
            }
        }
        pw.println(potential);
		pw.close();
	}
}
