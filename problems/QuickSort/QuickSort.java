package sorting;

public class QuickSort {

    public static void main(String[] args) {
        int[] arr = new int[]{4,6,1,2,8,3,9};
        quickSort(arr,0,arr.length-1);
        for(int i=0;i< arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }

    private static void quickSort(int[] arr, int low, int high) {
        if(low<high){
            int partitionInd = partition(arr,low,high);
            // sort the aarays without pivot element
            quickSort(arr, partitionInd+1, high);
            quickSort(arr, low, partitionInd-1);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot=arr[low]; // first element
        int i=low;
        int j=high;

        while(i<j){
            while(arr[i]<=pivot && i<=high-1){
                i++;
            }
            while (arr[j] > pivot && j>=low+1) {
                j--;
            }
            //swap if i and j have not crossed
            if(i<j){
                swap(arr,i,j);
            }
            //alternate to above
            // for(int k=low;k<=high;k++){
            //     if(pivot<=arr[k]){
            //         i++;
            //         swap(arr, i, k);
            //     }
            // }

        }
        //now swap pivot element with j(latest high index)
        swap(arr,low,j);
        // swap(arr,i,high);
        return j;
    }

    private static void swap(int[] arr, int pivotInd, int j) {
        int temp = arr[pivotInd];
        arr[pivotInd]=arr[j];
        arr[j]=temp;
    }
}