class Solution:
    def solve(self, s):
        output = ''
        num = ''
        for i in s:
            if i.isalpha():
                output += i*int(num)
                num =""
            else:
                num += i
        return output