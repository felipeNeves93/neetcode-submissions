class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        frequency_s = {}
        frequency_t = {}

        for letter in s:
            frequency_s[letter] = frequency_s.get(letter,0) + 1

        for letter in t:
            frequency_t[letter] = frequency_t.get(letter,0) + 1
        
        print(frequency_s)

        for key, value in frequency_s.items():
            if value != frequency_t.get(key):
                return False

        return True

        


        