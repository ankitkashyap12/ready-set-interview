class Solution {
    public int maxProfit(int[] prices) {
        
        return optimized(prices);
        
    }

    static int optimized(int[] prices){
        int minPrice = Integer.MAX_VALUE;
        int maxProfit=0;
        for(int price : prices){
            if(price < minPrice)
                minPrice=price;
            else{
                maxProfit=Math.max(maxProfit,price-minPrice);
            }
        }
        return maxProfit;
    }

    int brute(int[] prices){
        int maxProfit=0;
        for(int i=0;i<prices.length;i++){
            for(int j=i+1;j<prices.length;j++){
                int profit=prices[j]-prices[i];
                if(profit>0){
                  maxProfit= Math.max(profit,maxProfit);
                }

            }
        }
        return maxProfit;
    }
    
}