import unittest

from .encode_decode_strings import Codec
class TestCodec(unittest.TestCase):
    
    def setUp(self):
        self.codec = Codec()
    
    def test_example_case(self):
        input_data = ["hello", "world"]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_empty_list(self):
        input_data = []
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_single_empty_string(self):
        input_data = [""]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_multiple_empty_strings(self):
        input_data = ["", "", ""]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_strings_with_colon(self):
        input_data = ["hello:world", "foo:bar"]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_strings_with_numbers(self):
        input_data = ["123", "456", "789"]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_long_strings(self):
        input_data = ["a"*1000, "b"*2000, "c"*3000]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_large_number_of_strings(self):
        input_data = ["string{}".format(i) for i in range(1000)]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)
    
    def test_strings_with_special_characters(self):
        input_data = ["!@#$%^&*()", "{}|:\"<>?", "[]\\;',./"]
        encoded = self.codec.encode(input_data)
        decoded = self.codec.decode(encoded)
        self.assertEqual(decoded, input_data)

if __name__ == '__main__':
    unittest.main()