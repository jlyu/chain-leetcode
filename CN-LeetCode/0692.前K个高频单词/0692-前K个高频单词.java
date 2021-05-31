class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for (String word: words) {
            int x = map.getOrDefault(word, 0);
            map.put(word, x + 1);
        }

        PriorityQueue<Word> pq = new PriorityQueue<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            Word word = new Word(entry.getKey(), entry.getValue());
            
            pq.offer(word);

            if (pq.size() > k) {
                pq.poll();
            }
        }

        List<String> res = new ArrayList<String>();
        while(!pq.isEmpty()) {
            Word word = pq.poll();
            res.add(0, word.content);
        }
        return res;
    }
}

class Word implements Comparable<Word> {
    String content;
    int freq;

    Word(String content, int freq) {
        this.content = content;
        this.freq = freq;
    }

    public int compareTo(Word w) {
        return this.freq == w.freq ? w.content.compareTo(this.content) : this.freq - w.freq;
    }
}