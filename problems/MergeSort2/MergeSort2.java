package sorting;

/**
 * @author Ankit Kashyap on 04-11-2023
 */
public class MergeSort2 {
    public static int[] mergeSort(int[] array) {
        // Write your code here.
        sort(array,0,array.length-1);
        return array;
    }

    private static void sort(int[] array,int low,int high){
        if(low>= high)
            return;
        int mid= (low+high)/2;
        sort(array,low,mid);
        sort(array,mid+1,high);
        merge(array,low,mid,high);
    }

    private static void merge(int[] array,int low,int mid,int high){
        int n1= mid-low+1;
        int n2=high-mid;
        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];
        int k=0;
        int i=0;
        int j=0;
//        int[] tempArr  = new int[array.length];
        //copy low to mid into left array
        for(int t=low;t<mid+1;t++){
            leftArray[k]=array[t];
            k++;
        }
        k=0;
        //copy mid+1 to right in righArray
        for(int t=mid+1;t<=high;t++){
            rightArray[k]=array[t];
            k++;
        }

        k=low; // starting point of this iteration, not always zero
        //compare elememts of both array and merge in array
        while(i<n1 && j<n2){
            if(leftArray[i] <= rightArray[j] ){
                array[k]=leftArray[i];
                i++;
            }
            else{
                array[k]=rightArray[j];
                j++;
            }
            k++;
        }
        while(i<n1){
            array[k]=leftArray[i];
            k++;
            i++;
        }
        while(j<n2){
            array[k]=rightArray[j];
            k++;
            j++;
        }
    }
}
