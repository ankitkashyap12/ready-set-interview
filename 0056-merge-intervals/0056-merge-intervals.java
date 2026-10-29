import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length <= 1) {
            return intervals;
        }
        return getMerged2(intervals);
    }

    int[][] getMergedIntervals(int[][] intervals){
        Arrays.sort(intervals,(a,b)-> Integer.compare(a[0],b[0]));
        int currentStart = intervals[0][0];
        int currentEnd = intervals[0][1];
        int i=0;
        List<int[]> mergedIntervals = new ArrayList<>();
        for(int[] interval : intervals){
            int startTime=interval[0];
            int endTime = interval[1];
            if(i!=0){
            if(currentEnd >= startTime){
                currentEnd=Math.max(currentEnd,endTime);
                //currentStart=startTime;
            }
            else{
                mergedIntervals.add(new int[]{currentStart,currentEnd});
                currentEnd=endTime;
                currentStart= startTime;  
            }
            }
            
            i++;
        }
        mergedIntervals.add(new int[]{currentStart, currentEnd});
        return mergedIntervals.toArray(new int[mergedIntervals.size()][]);
    }
    

    int[][] getMerged2(int[][] intervals){
        Arrays.sort(intervals,(a,b) -> (a[0]-b[0]));
        int[] current = intervals[0];
        List<int[]> merged = new ArrayList<>();
        merged.add(current);
        for(int[] interval:intervals){
            if(current[1]>=interval[0]){
                current[1]=Math.max(current[1],interval[1]);
            }
            else{
                current= interval;
                merged.add(current);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }
}
