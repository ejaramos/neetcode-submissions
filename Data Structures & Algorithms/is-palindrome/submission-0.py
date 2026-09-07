class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        
        left_ptr = 0
        right_ptr = len(s) - 1 
        
        while left_ptr <= right_ptr:
            print( "left: {} right: {}".format(s[left_ptr], s[right_ptr]) )
            if s[left_ptr] != s[right_ptr]:
                return False 
            left_ptr += 1
            right_ptr -= 1

        return True

