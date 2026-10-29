import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Sort the array: O(n log n)
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            // Early pruning: Since array is sorted, if the first number is > 0, 
            // no three positive numbers can sum to 0.
            if (nums[i] > 0) {
                break;
            }
            
            // Skip duplicate values for the first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) {
                    // Need to decrease sum, move right pointer left
                    r--;
                } else if (sum < 0) {
                    // Need to increase sum, move left pointer right
                    l++;
                } else {
                    result.add(List.of(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    // Skip duplicates for both pointers
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                }
            }
        }
        return result;
    }

    List<Integer> getTriplet(int i, int[] nums) {
        int left = i + 1;
        int right = nums.length - 1;
        int target = -nums[i];
        List<Integer> result = new ArrayList<>();

        while (left < right && left < nums.length) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                result.add(nums[i]);
                result.add(nums[left]);
                result.add(nums[right]);
                return result; 
            }
            if (sum > target) {
                right--;
            } else {
                left++;
            }
        }
        return null;
    }
}