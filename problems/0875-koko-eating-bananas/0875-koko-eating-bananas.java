import java.util.Arrays;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        //return brute(piles,h);
        return binarySearch(piles,h);
    }


    static int binarySearch(int[] banana, int h) {
        // Binary search on the answer space: range [1, max(piles)]
        int left = 1;
        int right = 0;
        for (int p : banana) {
            right = Math.max(right, p);
        }

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (timeTaken(banana, mid) > h) {
                left = mid + 1; // Eating too slowly, need higher speed
            } else {
                right = mid; // Can finish in h hours, try a smaller speed
            }
        }
        return left;
    }

    public static long timeTaken(int[] banana, int rate) {
        long time = 0;
        for (int numOfBanana : banana) {
            // Ceiling division: (numOfBanana + rate - 1) / rate
            time += (long) (numOfBanana + rate - 1) / rate;
        }
        return time;
    }

    static int brute(int[] banana,int h){
        //sort
        Arrays.sort(banana);
        // time will be min 1hr - to max time taken for a tree
        //start from 1 and calculate for each and compare ith total time
        for(int i=1;i<=banana[banana.length-1];i++){
            int totalTime=0;
            for(int j=0;j<banana.length;j++){
                totalTime+=((banana[j]+i-1)/i);
                //System.out.println("total time taken when "+i+" banana per hour for "+banana[j]+" banana is "+((banana[j]+i-1)/i));
            }

            //System.out.println("Total time taken when "+i+" banana per hour is "+totalTime);
            if(totalTime<=h){
                return i;

            }
                
            

        }
        return 0;

    }
    }
