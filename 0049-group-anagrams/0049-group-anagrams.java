class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> grouped = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);

            grouped.computeIfAbsent(key, k -> new ArrayList<>())
                   .add(s);
        }

        return new ArrayList<>(grouped.values());
    }

    public List<List<String>> groupAnagramsBySignature(String[] strs){
        Map<String, List<String>> grouped = new HashMap<>();
        for(String s : strs){
            int[] freq= new int[26];
            for(char c:s.toCharArray()){
                freq[c-'a']+=1;
            }
            StringBuilder sb= new StringBuilder();
            for(int count:freq){
                sb.append(count).append("#");
            }
            grouped.computeIfAbsent(sb.toString(), k -> new ArrayList<>())
                   .add(s);
        }
        return new ArrayList<>(grouped.values());
    }

    }
    