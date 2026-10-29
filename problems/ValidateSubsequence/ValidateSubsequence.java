package arrays;

import java.util.List;
import java.util.Objects;

/**
 * @author Ankit Kashyap on 27-08-2023
 * Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
 * <p>
 * A subsequence of an array is a set of numbers that aren’t necessarily adjacent in the array but that are in the same order as they appear in the array. For example these numbers
 * <p>
 * [2, 3, 5]
 * are a subsequence of the array:
 * <p>
 * [1, 2, 3, 4, 5]
 */
public class ValidateSubsequence {

    public static boolean validateSubSequenceBrute(List<Integer> array, List<Integer> sequence) {
        //O(N) (N is size of array) and O(1)
        int count = 0;
        int latestIndex = 0;
        for (Integer num1 : sequence) {
            for (int i = latestIndex; i < array.size(); i++) {
                if (Objects.equals(num1, array.get(i))) {
                    count++;
                    latestIndex = i + 1;
                    break;
                }
            }
        }
        return count == sequence.size();
    }

    public static boolean validateSubSequenceBruteBetter(List<Integer> array, List<Integer> sequence) {
        //O(N) (N is size of array) and O(1)
        //here no need to iterate over sequnce , we will only increment index in sequnce if no found
        int latestIndex = 0;
        for (Integer num1 : sequence) {
            if(latestIndex==sequence.size())
                return true; //condition when all sequence has been found
            if(num1==sequence.get(latestIndex))
                latestIndex++;
        }
        return latestIndex == sequence.size();
    }

}
