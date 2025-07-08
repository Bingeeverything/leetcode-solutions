from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dic = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            my_dic[key].append(string)
         
        return list(my_dic.values())
                