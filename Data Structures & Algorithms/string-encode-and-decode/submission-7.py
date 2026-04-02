class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "-_-"
        new_string = ''
        for string in strs:
            new_string +=string
            new_string+= delimiter
        print("Encoded string", new_string)
        return new_string


    def decode(self, s: str) -> List[str]:
        delimiter = "-_-"
        output_list = s.split(delimiter)
        print("Output",output_list)
        return output_list[:-1]

