class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indice = 0
        if needle in haystack:
            for NUMletraH in range(len(haystack)-len(needle)):
                passou = True
                for NUMletraN in range(len(needle)):
                    if not(needle[NUMletraN] == haystack[NUMletraH+NUMletraN]):
                        passou = False
                        break
                if passou:
                    break
                else:
                    indice +=1
            return indice
        return -1
        
