class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) { return 0; }
        if (!wordList.contains(beginWord)) { wordList.add(beginWord); }

        Map<String, List<String>> graph = constructGraph(wordList);
        Set<String> visited = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        visited.add(beginWord);
        q.offer(beginWord);

        int seq = 1;
        while (!q.isEmpty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                String currWord = q.poll();
                if (currWord.equals(endWord)) { return seq; }

                for (String neighbor: graph.getOrDefault(currWord, new ArrayList<>())) {
                    if (visited.contains(neighbor)) { continue; }

                    visited.add(neighbor);
                    q.offer(neighbor);
                }
            }
            seq++;
        }
        return 0;
    }

    private Map<String, List<String>> constructGraph(List<String> wordList) {
        Map<String, List<String>> graph = new HashMap<>(); 
        int n = wordList.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                String w1 = wordList.get(i);
                String w2 = wordList.get(j);
                if (oneChangeAway(w1, w2)) {
                    graph.computeIfAbsent(w1, k -> new ArrayList<>()).add(w2);
                    graph.computeIfAbsent(w2, k -> new ArrayList<>()).add(w1);
                }
            }
        }
        return graph;
    }

    private boolean oneChangeAway(String w1, String w2) {
        int diff = 0;
        for(int i = 0; i < w1.length(); i++) {
            if (w1.charAt(i) != w2.charAt(i)) {
                diff++;
            }
        }
        return diff == 1;
    }
}