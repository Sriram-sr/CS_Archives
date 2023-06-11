s = "cbaebabacd"
p = "abc"
# [0,1,2,3,4,5,6,7]
# [0,2,4,6]

anagram_indexes = []

for idx in range(len(s)):
    if idx<=len(s)-len(p):
        compare_str = s[idx:idx+len(p)]
        # true_list = [let in compare_str for let in p]
        # if all(true_list) and set(p)==set(compare_str):
        #     anagram_indexes.append(idx)
        if sorted(compare_str)==sorted(p):
            anagram_indexes.append(idx)

print(anagram_indexes)            