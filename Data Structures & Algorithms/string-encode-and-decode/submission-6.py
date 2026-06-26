class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            curr = ""
            for char in word:
                curr_char = 'a' if char == 'z' else chr(ord(char) + 1)
                curr = curr + curr_char

            encoded_str += curr
            encoded_str += " "
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        curr = ""
        for char in s:
            if char != " ": 
                curr_char = 'z' if char == 'a' else chr(ord(char) - 1)
                curr += curr_char
            else:
                decoded_strs.append(curr)
                curr = ""

        return decoded_strs