package sorting;

import java.util.ArrayList;
import java.util.List;

/**
 * Algorithm :
 * 1. Partition the array by mid point
 * 2. rpeat this for all new smaller array untill single element
 * 3. Start merging from bottom by swpping
 * 4. now will get two sorted array  that needs to merge
 * 5. if while merging all left array's elements gets added, then append all remaining elements of right array and vice versa .
 * 
 */
public class MergeSort {
    
    public static void mergeSort(int[] array,int low, int high){  
        if(low>=high) return;
        int mid = (low+high)/2;
            //sort first half
        mergeSort(array, low, mid);
            //sort second half
        mergeSort(array, mid+1, high);

            //merge
        merge(array,low,mid,high);

        

    }
    private static void merge(int[] array, int low, int mid, int high) {
        //this can also be done by taking two temp array contsining left & right part an then comapring
        int left= low;
        int right= mid+1;
        List<Integer> sortedArray= new ArrayList<>();
        while(left <=mid && right<=high){
            if(array[left] <= array[right]){
                sortedArray.add(array[left]);
                left++;
            }
            else{
                sortedArray.add(array[right]);
                right++;
            }
        }
        while(left<=mid){
           sortedArray.add(array[left]);
            left++;
        }
        while (right<=high) {
            sortedArray.add(array[right]);
            right++;
        }
        // System.out.println("sorted array "+Arrays.asList(sortedArray));
        for(int i=low;i<=high;i++){
            array[i]=sortedArray.get(i-low);
            // System.out.print(sortedArray[i]+" ");
        }

        // return array;
    }
    public static void main(String[] args) {
        int[] arr = new int[]{1,9,8,2,5};
        MergeSort.mergeSort(arr,0,arr.length-1);
        // System.out.println(arr);
        for(int i =0;i< arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
