class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        window_size = word_len * word_count
        if window_size > len(s):
            return []
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        result_indices = []
        for i in range(len(s) - window_size + 1):
            freq_copy = word_freq.copy()
            for j in range(i, i + window_size, word_len):
                word = s[j:j + word_len]
                if word not in freq_copy:
                    break
                freq_copy[word] -= 1
                if freq_copy[word] == 0:
                    del freq_copy[word]
            if not freq_copy:
                result_indices.append(i)
        return result_indices
