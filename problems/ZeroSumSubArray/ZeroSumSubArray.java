package arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Ankit Kashyap on 24-09-2023
 *
 * <div class="html">
 *   <p>
 *     You're given a list of integers <span>nums</span>. Write a function that
 *     returns a boolean representing whether there exists a zero-sum subarray of
 *     <span>nums</span>.
 *   </p>
 *
 *   <p>
 *     A zero-sum subarray is any subarray where all of the values add up to zero.
 *     A subarray is any contiguous section of the array. For the purposes of this
 *     problem, a subarray can be as small as one element and as long as the
 *     original array.
 *   </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">nums</span> = [-5, -5, 2, 3, -2]</pre>
 * <h3>Sample Output</h3>
 * <pre>True <span class="CodeEditor-promptComment">// The subarray [-5, 2, 3] has a sum of 0
 * </span>
 * </pre></div>
 */
public class ZeroSumSubArray {

    public boolean zeroSumSubarray(int[] nums) {
        // we track sum from oth index to last or ith. Now sum(0,1) the sum(1,2) will be sum(0,1) plus elemnet at 2.. and so on.
        //we track the sum and if we find that sum upto some elemetn has repeated it means sum did not change between them i.e there was zero sum subarray between them
        Set<Integer> sums = new HashSet<>();
        //this could added as if as well, say currentSum==0 || num==0
        sums.add(0); // so that if element is zero or sum becomes zero and gets added then we know zero sum achieved
        int currentSum = 0;
        for (int num : nums) {
            currentSum += num;
            // if(num==0 || currentSum==0 )
            //   return true;
            if (!sums.add(currentSum))
                return true;
        }
        return false;

    }
}
