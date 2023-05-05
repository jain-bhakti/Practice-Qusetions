"""
Idea : divide the word into two fragments say prefix and suffix and check wherther both of the parts exist in words array by
       applying dfs recursively.

Algoritm:
1. pick a word from the words array.
2. iterate through that word and amintain prefix and suffix in each iteration.
3. check whether the prefix and suffix both exist in words set,if yes return True.
4. call dfs recursively for subparts from suffix.
5. for each word if the function returns True append it to the result.

"""

def ConcatenatedWords(words):
    word_set = set(words)

    def dfs(each_word):
        for index in range(1,len(each_word)):
            prefix = each_word[:index]
            suffix = each_word[index:]

            if (prefix in word_set and suffix in word_set) or (prefix in word_set and dfs(suffix)):
                return True

        return False

    res = []
    for word in word_set:
        if dfs(word):
            res.append(word)
    return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(ConcatenatedWords(words))
