"""
Anagram problem exercise
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

For example: restful and fluster

Good luc
"""

def anagram_check(word1,word2):
     return sorted(word1) == sorted(word2)

str1 = "fluster".lower()
str2 = "restful".lower()

print(anagram_check(str1,str2))




print(sorted(str1))
print(sorted(str2))