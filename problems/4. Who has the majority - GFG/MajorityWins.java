/**
 * Who has the majority? (GeeksforGeeks)
 *
 * Given an array arr[] of size N and two elements x and y, find which element appears most in the array, x or y.
 * If both elements have the same frequency, return the smaller element.
 *
 * Time Complexity: O(N) single pass.
 * Auxiliary Space: O(1).
 */
public class MajorityWins {

    public static int majorityWins(int arr[], int n, int x, int y) {
        int countX = 0;
        int countY = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == x) {
                countX++;
            } else if (arr[i] == y) {
                countY++;
            }
        }

        if (countX > countY) {
            return x;
        } else if (countY > countX) {
            return y;
        } else {
            return Math.min(x, y);
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5};
        System.out.println(majorityWins(arr1, arr1.length, 4, 5)); // Output: 4

        int[] arr2 = {1, 2, 3, 4, 5, 6, 7, 8};
        System.out.println(majorityWins(arr2, arr2.length, 1, 7)); // Output: 1
    }
}

