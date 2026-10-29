class Solution {
    /**
     * Approach 1: Two Pointers (Greedy)
     * Invariant: The volume is constrained by min(height[left], height[right]). Moving the taller
     * wall inward reduces width without possibility of increasing height. Moving the shorter wall
     * inward is the only way that might discover a taller wall and increase volume.
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxVolume = 0;

        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int width = right - left;
            maxVolume = Math.max(maxVolume, h * width);

            // Fast-forward pointers past heights <= current minimum to reduce inner iterations
            while (left < right && height[left] <= h) {
                left++;
            }
            while (left < right && height[right] <= h) {
                right--;
            }
        }
        return maxVolume;
    }
}