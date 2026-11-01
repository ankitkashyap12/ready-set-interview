/* Kadane's Algo

The idea is simple: Using a variable (currSum) track the sum of the elements. If at any instance, this sum is negative, make it 0. This is because, for the next value, there are only 2 options: Either the next value will be positive or negative.

If the next value is positive: Then, the running sum (-ve) + next value (+ve) will offcourse be greater than current sum, as +ve is always greater than -ve.
If the next value is negative: Then, the running sum (-ve) + next value (also -ve) will become higher value in negative, which will be smaller.
Hence, if by adding an element the total sum becomes negative then, that element cannot be considered in maximum subarray and we should start a new subarray.
    */

class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum=0;
        int currentSum=0;
        for(int i=0;i<nums.length;i++){
            currentSum+=nums[i];
            if (currentSum > maxSum || i==0){
                maxSum=currentSum;
            }
            if(currentSum<0){
                currentSum=0;  
            }
            
        }
        return maxSum;
    }
}
