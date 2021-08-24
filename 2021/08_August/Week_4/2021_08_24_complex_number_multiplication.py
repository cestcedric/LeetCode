class Solution:
    # O(n) time: split looks through complete string
    def complexToInt(self, num: str) -> tuple:
        real, img = num.split('+')
        return (int(real), int(img[:-1]))
    
    
    # O(1) time
    # extra method seems a little over the top, but can be adapted for better format
    def intToComplex(self, real, img) -> str:
        return '{}+{}i'.format(real, img)
    
    
    # O(n) time: split strings to get int (very short input, so could say O(1))
    # O(1) space: always allocate 4 integers
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = self.complexToInt(num1)
        num2 = self.complexToInt(num2)
        
        real = num1[0] * num2[0] - num1[1] * num2[1]
        img = num1[0] * num2[1] + num1[1] * num2[0]
        
        return self.intToComplex(real, img)