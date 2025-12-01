import java.io.*;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Map;
import java.util.Collection;
import java.util.ArrayList;
import java.util.List;



public class Last {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new FileReader("notlast.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("notlast.out")));

		StringTokenizer st = new StringTokenizer(r.readLine());
        String[] cows= {"Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"};
		int N = Integer.parseInt(st.nextToken());

        Map<String,Integer> milking_log=new HashMap<String,Integer>();
        for (String cow:cows){
            milking_log.put(cow,0);
        }
        for (int i=0;i<N;i++){
            st=new StringTokenizer(r.readLine());
            String name= st.nextToken();
            int amount=Integer.parseInt(st.nextToken());
            milking_log.put(name,milking_log.get(name)+amount);
        }
        int minimum=Integer.MAX_VALUE;
        for (int val:milking_log.values()){
            if (val<minimum){
                minimum=val;
            }
        }
        if (milking_log.size()==1){
            pw.println("Tie");
            return;
        }


        Map<String,Integer> new_milking_log=new HashMap<String,Integer>();
        for (String key: milking_log.keySet()){
            if (milking_log.get(key)!=minimum){
                new_milking_log.put(key,milking_log.get(key));
            }
        }
        int num_return=Integer.MAX_VALUE;
        for (int val:new_milking_log.values()){
            if (val<num_return){
                num_return=val;
            }
        }

        List<String> matches = new ArrayList<>();
        for (String key: new_milking_log.keySet()){
            if (new_milking_log.get(key)==num_return){
                matches.add(key);
            }
        }
        if (matches.size()==1){
            pw.println(matches.get(0));
        }
        else{
            pw.println("Tie");
        }




		
		/*
		 * Make sure to include the line below, as it
		 * flushes and closes the output stream.
		 */
		pw.close();
	}
}