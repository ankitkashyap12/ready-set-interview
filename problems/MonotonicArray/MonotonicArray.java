package arrays;

/**
 * @author Ankit Kashyap on 07-09-2023
 * <p>
 *
 * Write a function that takes in an array of integers and returns a boolean
 * representing whether the array is monotonic.
 * <p>
 * An array is said to be monotonic if its elements, from left to right, are
 * entirely non-increasing or entirely non-decreasing.
 * <p>
 * Non-increasing elements aren't necessarily exclusively decreasing; they simply
 * don't increase. Similarly, non-decreasing elements aren't necessarily
 * exclusively increasing; they simply don't decrease.</p>
 */
public class MonotonicArray {


    public static boolean isMonotonic(int[] array) {
        //in each loop compare with adjacent and then boolean with previous result.
        if (array.length <= 2) // 0,1 and 2 will always be monotonic.
            return true;
        boolean isIncreasing = true;
        boolean isDecreasing = true;
        for (int i = 0; i < array.length - 1; i++) {
            isIncreasing = isIncreasing && (array[i] <= array[i + 1]);
            isDecreasing = isDecreasing && (array[i] >= array[i + 1]);
        }
        return isIncreasing || isDecreasing;
    }

    public static boolean isMonotonic2(int[] array) {
        // instead of checking in every loop, we can return as soon as we see order not following
        if (array.length <= 2)
            return true;
        boolean isIncreasing = array[0] < array[array.length - 1];
        for (int i = 0; i < array.length - 1; i++) {
            if (isIncreasing && array[i] > array[i + 1])
                return false; // previously it was increasing but in this index they are not in ncreasing order hence break
            if (!isIncreasing && array[i] < array[i + 1])
                return false; // was supposed to be decreasing but next element was bigger than previous index hence break
        }
        return true; // not returned false yet hence must be monotonic
    }

    public static boolean isMonotonic3(int[] array) {
        // same as solution 2 but more expressive
        boolean isNonIncreasing = true;
        boolean isNonDecreasing = true;
        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1])
                isNonDecreasing = false;

            if (array[i] > array[i - 1])
                isNonIncreasing = false;
        }
        return isNonIncreasing || isNonDecreasing;
    }

    public static boolean isMonotonicDirection(int[] array) {
        //complex
        if(array.length<=2)
            return true;
        int direction = array[1]-array[0]; //assuming one direction >0 and other be < 0, this will help[ to check if order has changed]
        for(int i=2;i<array.length;i++){
            if(direction==0){
                direction = array[i]-array[i-1];
                continue;
            }
            if(breaksDirection(direction,array[i-1],array[i]))
                return false;
        }
        return true;
    }
    public static boolean breaksDirection(int direction ,int previous,int current){
        int difference = current-previous;
        if(direction > 0)
            return difference < 0;  //if direction was > 0, order will be breaked only when differnece between these two were negatiove
        return difference > 0;
    }
}
