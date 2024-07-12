class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for word in strs:
            res += f'{len(word)}#' + word
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        words = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j + 1 + length]
            words.append(word)
            i = j + 1 + length
        return words