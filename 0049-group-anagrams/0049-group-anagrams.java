class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> grouped= new HashMap<>();
        List<List<String>> result= new ArrayList<>();
        for(String s: strs){
            char[] charSorted = s.toCharArray();
            Arrays.sort(charSorted);
            String sorted = new String(charSorted);
            
            if(grouped.containsKey(sorted)){
                List<String>listOfAnagrams =grouped.get(sorted);
                listOfAnagrams.add(s);
                grouped.put(sorted,listOfAnagrams);
            }
            else{
            List<String> listOfAnagrams= new ArrayList<>();
            listOfAnagrams.add(s);
            grouped.put(sorted,listOfAnagrams);
            }
        }
        for(Map.Entry<String,List<String>> kv: grouped.entrySet()){
            result.add(kv.getValue());
        }
        return result;
    }
    }