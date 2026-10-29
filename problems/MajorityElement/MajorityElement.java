package arrays;

/**
 * @author Ankit Kashyap on 24-09-2023
 *
 * <div class="html">
 *   <p>
 *     Write a function that takes in a non-empty, unordered <span>array</span> of
 *     positive integers and returns the array's majority element without sorting
 *     the array and without using more than constant space.
 *   </p>
 *   <p>
 *     An array's majority element is an element of the array that appears in over
 *     half of its indices. Note that the most common element of an array (the
 *     element that appears the most times in the array) isn't necessarily the
 *     array's majority element; for example, the arrays
 *     <span>[3, 2, 2, 1]</span> and <span>[3, 4, 2, 2, 1]</span> both have
 *     <span>2</span> as their most common element, yet neither of these arrays
 *     have a majority element, because neither <span>2</span> nor any other
 *     element appears in over half of the respective arrays' indices.
 *   </p>
 *   <p>
 *     You can assume that the input array will always have a majority element.
 *   </p>
 *   <h3>Sample Input</h3>
 *   <pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 3, 2, 2, 1, 2]</pre>
 *   <h3>Sample Output</h3>
 *   <pre>2<span class="CodeEditor-promptComment"> // 2 occurs in 4/7 array indices, making it the majority element</span>
 * </pre>
 * </div>
 */
public class MajorityElement {

    //since question mentions there will always be one majority elemnt we can directly return , otherwise will check for frequency of that element
    // using one more for loop as it no majority element exist at all
    public int majorityElement(int[] array) {
        // Moore's Voting algo
        int majorityElement = array[0];
        int count = 0;
        for (int num : array) {
            if (count == 0) {
                majorityElement = num;
            }
            if (num == majorityElement)
                count++;
            else
                count--;
        }
        return majorityElement;
    }

    public int majorityElementUsingBitMagic(int[] array) {
        // Write your code here.
        int majorityElement = 0;
        for (int currentBit = 0; currentBit < 32; currentBit++) {
            int currentBitValue = 1 << currentBit;
            int setBitCount = 0;
            for (int num : array) {
                if ((num & currentBitValue) != 0)
                    setBitCount += 1;
            }
            // If the total set bits exceeds n/2,
            // this bit should be present in majority Element.
            if (setBitCount > array.length / 2)
                majorityElement += currentBitValue;
        }

        return majorityElement;
    }
}
