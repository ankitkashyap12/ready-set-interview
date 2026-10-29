package arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Ankit Kashyap on 29-08-2023
 * <p>
 * <p>
 * Write a function that takes in a non-empty array of distinct integers and an
 * integer representing a target sum. The function should find all triplets in
 * the array that sum up to the target sum and return a two-dimensional array of
 * all these triplets. The numbers in each triplet should be ordered in ascending
 * order, and the triplets themselves should be ordered in ascending order with
 * respect to the numbers they hold.
 */
public class TripleSum {

    public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
        //brute force would be to have 3 loops
        // use two pointer slider after sorting
        // we itrerate upto len-2 because anyhow right pointer covers last elemnt and triplets will atleat 3, so unnecesary to go last elemnt
        Arrays.sort(array);
        int cSum;
        List<Integer[]> tripletsList= new ArrayList<>();
        for(int i=0;i<array.length-2;i++){
            int left=i+1;
            int right=array.length-1;

            while(left <right){
                cSum=array[i]+array[left]+array[right];
                if(cSum==targetSum){
                    tripletsList.add(new Integer[]{array[i],array[left],array[right]});
                    left++;
                    right--;
                }
                else if(cSum < targetSum)
                    left++;
                else
                    right--;
            }

        }
        return tripletsList;

    }
}
