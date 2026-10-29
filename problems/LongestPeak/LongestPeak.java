package arrays;

/**
 * @author Ankit Kashyap on 10-09-2023
 * <p>
 * Write a function that takes in an array of integers and returns the length of
 * the longest peak in the array.
 * <p>
 * A peak is defined as adjacent integers in the array that are <b>strictly</b>
 * increasing until they reach a tip (the highest value in the peak), at which
 * point they become <b>strictly</b> decreasing. At least three integers are required to
 * form a peak.
 * <p>
 * For example, the integers <span>1, 4, 10, 2</span> form a peak, but the
 * integers <span>4, 0, 10</span> don't and neither do the integers
 * <span>1, 2, 2, 0</span>. Similarly, the integers <span>1, 2, 3</span> don't
 * form a peak because there aren't any strictly decreasing integers after the
 * <span>3</span>.
 * </p>
 * </p>
 */
public class LongestPeak {

    public static int longestPeak(int[] array) {
        // Write your code here.
        int longestPeakLen=0;
        for(int i=1;i<array.length-1;i++){
            System.out.println("left,mid,right "+array[i-1]+"->"+array[i]+"->"+array[i+1]);
            if(array[i]>array[i-1] && array[i]>array[i+1]){
                //array[i] is peak. now check length around left and right
                //left of this element should be decreasing,count all upto which it was decreasing
                System.out.println("current peak is "+array[i]);
                int left=i-2;
                while(left>=0 && array[left] < array[left+1] ){
                    left--;
                }
                int right= i+2;
                while(right < array.length && array[right]< array[right-1]){
                    right++;
                }

                int currLongPeakLen=right-left-1;
                longestPeakLen= Math.max(currLongPeakLen, longestPeakLen);
                // i=right; we can use this statement to reduce no of compaariosn, but will need while loop as in this for loop i will be increaesd hence elelmbnt at current right will be skipped
            }
            System.out.println("current i is "+i);
        }
        return longestPeakLen;
    }
}
