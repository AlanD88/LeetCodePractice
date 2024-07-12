# 271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/description/

## Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:

vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:

string encoded_string = encode(strs);

and Machine 2 does:

vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:

Input: dummy_input = [""]
Output: [""]

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.


## Solution

```python3
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
```

## Explanation

We add a value before a delimiter based on the length of the word we're encoding.  So if a word is 14 characters long we encode 14# prior to the word. As our encoded string will start with this encoded value, we don't need to worry about seeing the delimeter value again when we go to decode as we already have the length of the word which should set us directly to the next delimeter, precluding the need to search for the next delimeter and risking decoding an incorrect value if a word actually contains the delimeter.

Example:
If we have ["hello", "tricky34#", "goodbye"]

We wont need to worry about the 34# because we'll encode the string as
5#hello9#trick34#7#goodbye

Starting at the first delimeter we get a lenght of 5 to parse out hello.  Knowing the lenght of the first word we can jump to the start of the integer length of the next word before the next delimeter.  getting us a length of 9 to parse out tricky34#, allowing us to also skip over the 34# and start right at 7# delimeter for the last word.

## Analyze Complexity

Time Complexity O(n)
 We iterate over the string once.

Space Complexity O(1)