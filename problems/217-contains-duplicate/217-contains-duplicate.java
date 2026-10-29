import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniqueSet = new HashSet<>(nums.length);
    for (int num : nums) {
      if (!uniqueSet.add(num)) 
          return true;
    }

    return false;
  }
    
}
    