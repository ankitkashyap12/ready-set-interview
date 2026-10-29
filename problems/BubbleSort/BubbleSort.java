package sorting;

/**
 * @author Ankit Kashyap on 04-11-2023
 */
public class BubbleSort {
    public static int[] bubbleSort(int[] array) {
        // Write your code here.
        boolean swapped = false;
        // no need to iterate for last i sorted elements
        for(int i=0;i< array.length-i-1;i++){
            swapped=false;
            for(int j=0;j<array.length-i-1;j++){
                if(array[j]> array[j+1]){
                    swap(array,j,j+1);
                    swapped=true;
                }
            }
            if(!swapped)
                break;
        }
        return array;
    }
    static void swap(int[] array,int i, int j){
        int temp= array[i];
        array[i]=array[j];
        array[j]=temp;
    }

    // second way
    public static int[] bubbleSortWhile(int[] array) {
        // Write your code here.
        boolean isSorted = false;
        while(!isSorted){
            isSorted= true;
            for(int i=0;i<array.length-1;i++){
                if(array[i] > array[i+1]){
                    swap(array,i,i+1);
                    isSorted=false;
                }
            }
        }
        return array;
    }

    public int[] bubbleSortRecursive(int[] array,int n){
        //base case
        if(n==1)
            return array;
        //first sort(largest element is at last
        for(int i=0;i<array.length-1;i++){
            if(array[i] > array[i+1]){
                swap(array,i,i+1);
            }
        }
        //recursive call to remaining elements
        bubbleSortRecursive(array,n-1);
        return array;
    }

}
