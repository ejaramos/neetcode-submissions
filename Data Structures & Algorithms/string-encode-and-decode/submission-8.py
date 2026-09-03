import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode list of strings
        # return base64.b64encode(strs.encode('utf-8'))
        if len(strs) == 0:
            return "EMPTY"
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        # if s == "\n":
        #     return [""]
        if s == "EMPTY":
            return []
        # decode and decompose back to 
        return s.split("\n")


