class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_digits = ""
        final=[]
        for i in digits:
            new_digits += str(i)
        new_digits = int(new_digits) + 1
        new_digits = str(new_digits)
        for j in new_digits:
            final.append(j)
        return final 
