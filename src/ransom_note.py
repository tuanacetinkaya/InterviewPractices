# assume you have a magazine that holds a number of letters
# and you want to write a certain word out of it.
# write a program that returns if you can write the given word with an array of given letters
# 02.09.2020 -> TechLead CoderPro free overview questions
from collections import defaultdict


class Solution:
    # time complexity with n letters in magazine and m lettered word is: O(n)+O(m)
    # space complexity would be O(k) k is the total letters which is: O(1)
    def canSpell(self, mag, word):
        req = []
        req[:] = word
        for spl in mag:
            if spl in req:
                req.remove(spl)
        if len(req) == 0:
            return True
        return False


class TechLeadSolution:
    # time complexity: O(n) + O(m)
    # space complexity: O(1)
    def canSpell(self, mag, note):
        letters = defaultdict(int)
        for c in mag:
            letters[c] += 1
        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True


magazine = ['a', 'b', 'c', 'd', 'e', 'f']
# True
word1 = 'bed'

# False
word2 = 'cat'

print(Solution().canSpell(magazine, word1))
print(Solution().canSpell(magazine, word2))
print(TechLeadSolution().canSpell(magazine, word1))
print(TechLeadSolution().canSpell(magazine, word2))
