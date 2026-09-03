import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def generateCounter( word:str ) -> tuple:
            alphabet = string.ascii_lowercase
            char_counts = [word.count(c) for c in list(alphabet)]
            # print(tuple(char_counts))
            return tuple(char_counts)
        
        # create a map using Counter
        word_frequency_map = { alpha_count: [] for alpha_count in [generateCounter(x) for x in strs]  }

        for word in strs:
            word_frequency_map[generateCounter(word)].append(word)

        return [x for x in word_frequency_map.values()]
        


        