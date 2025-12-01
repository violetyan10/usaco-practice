import java.util.*;

public class Alchemy {

    static int N;
    static int[] metalUnits;
    static List<int[]> recipes = new ArrayList<>();
    static ArrayList<Integer>[] elementsNeed;  // Array of ArrayLists to store dependencies

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input N
        N = scanner.nextInt();

        // Input metal units
        metalUnits = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            metalUnits[i] = scanner.nextInt();
        }

        // Input K (number of recipes)
        int K = scanner.nextInt();

        // Input recipes
        for (int i = 0; i < K; i++) {
            int metalType = scanner.nextInt();  // metal type (index)
            int numElements = scanner.nextInt();  // number of elements required

            // Use a list to store the required elements
            List<Integer> recipe = new ArrayList<>();
            for (int j = 0; j < numElements; j++) {
                recipe.add(scanner.nextInt());
            }

            // Add the recipe to the list
            recipes.add(new int[]{metalType, numElements}); // Store metal type and number of elements
            elementsNeed[metalType] = new ArrayList<>(recipe);  // Map metal type to its dependencies
        }

        // Sort recipes based on the metal type
        recipes.sort(Comparator.comparingInt(r -> r[0]));

        // Initialize elementsNeed
        elementsNeed = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            elementsNeed[i] = new ArrayList<>();
        }

        // Fill elementsNeed array
        for (int[] recipe : recipes) {
            int index = recipe[0];
            for (int i = 0; i < recipe[1]; i++) {
                elementsNeed[index].add(recipe[2 + i]);
            }
        }

        // Base case when we have enough of the metal
        int ans = 0;
        while (createMetal(N)) {
            ans++;
        }

        System.out.println(ans);
    }

    // Function to check if we can create a given metal
    static boolean createMetal(int metal) {
        if (metalUnits[metal] > 0) {
            metalUnits[metal]--;
            return true;
        }

        ArrayList<Integer> elements = elementsNeed[metal];  // Changed to ArrayList
        if (elements.isEmpty()) {
            return false;
        }

        // Try creating the required elements
        for (int element : elements) {
            if (!createMetal(element)) {
                return false;
            }
        }

        return true;
    }
}
