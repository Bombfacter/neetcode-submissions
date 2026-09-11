class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            x = len(word)
            x = str(x)
            encoded += x + "#" + word

        return encoded



    def decode(self, s: str) -> List[str]:
        decoded = []

        i=0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            lengthWord = int(s[i:j])

            decoded.append(s[j + 1 : j + 1 + lengthWord])

            i = j + 1 + lengthWord

        return decoded