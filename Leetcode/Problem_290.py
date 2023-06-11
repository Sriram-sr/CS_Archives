class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split()
        match_dict = dict()
        flag = True
        
        if len(pattern)!=len(splitted):
            return False
            
        for idx in range(len(pattern)):
            if idx==0:
                match_dict[pattern[idx]] = splitted[idx]
            if pattern[idx] in match_dict:
                if not splitted[idx]==match_dict[pattern[idx]]:
                    flag = False
                    break
            else:
                if splitted[idx] in match_dict.values():
                    flag = False
                    break
                else:
                    match_dict[pattern[idx]] = splitted[idx]	

        return flag        