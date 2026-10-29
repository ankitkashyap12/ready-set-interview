package arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Ankit Kashyap on 11-09-2023
 * <div class="html">
 * <p>
 *   Given an array of integers between <span>1</span> and <span>n</span>,
 *   inclusive, where <span>n</span> is the length of the array, write a function
 *   that returns the first integer that appears more than once (when the array is
 *   read from left to right).
 * </p>
 * <p>
 *   In other words, out of all the integers that might occur more than once in the
 *   input array, your function should return the one whose first duplicate value
 *   has the minimum index.
 * </p>
 * <p>
 *   If no integer appears more than once, your function should return
 *   <span>-1</span>.
 * </p>
 * <p>Note that you're allowed to mutate the input array.</p>
 * <h3>Sample Input #1</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 2, 3, 3, 4]
 * </pre>
 * <h3>Sample Output #1</h3>
 * <pre>2 <span class="CodeEditor-promptComment">// 2 is the first integer that appears more than once.</span>
 * <span class="CodeEditor-promptComment">// 3 also appears more than once, but the second 3 appears after the second 2.</span>
 * </pre>
 * <h3>Sample Input #2</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 3, 3, 2, 4]
 * </pre>
 * <h3>Sample Output #2</h3>
 * <pre>3 <span class="CodeEditor-promptComment">// 3 is the first integer that appears more than once.</span>
 * <span class="CodeEditor-promptComment">// 2 also appears more than once, but the second 2 appears after the second 3.</span>
 * </pre>
 * </div>
 */
public class FirstDuplicateValue {

    //using HashSet
    public int firstDuplicateValue(int[] array) {
        // Write your code here.
        Set<Integer> lookUpSet = new HashSet<>();
        for (int num : array) {
            if (!lookUpSet.add(num))
                return num;
        }
        return -1;
    }

    //since it's 1 to n and array can be mutated
    //we can map integers from 1 to n to array inices
    // we know it will be like index-1=element
    //hence we will make it negative then if we come again it will already be negative

    int firstDuplicateValueIndexMap(int[] array) {
        // Write your code here.
        for (int num : array) {
            int absInt = Math.abs(num); // this is important as we can come across num that was already makrked as negeative
            if (array[absInt - 1] < 0) return absInt;
            array[absInt - 1] *= -1;
        }
        return -1;
    }
}
